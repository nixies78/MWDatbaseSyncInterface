import pyodbc, pandas as pd, requests
from Patient import Patient
import eclinic_logger

SYNC_ENABLED = True
API_ENDPOINT = 'http://cloud.staging.adoniamedical.co.uk:8000/patients'
HEADERS = {"Host": "eclinic", "Content-Type": "application/json"}
READ_FULL_QUERY = "SELECT * FROM wp_mediweight"
READ_FILTERED_QUERY = "SELECT * FROM `wp_mediweight` WHERE `exported_eclinic` = false"
RECORD_UPDATE_QUERY = "UPDATE `wp_mediweight` SET `exported_eclinic` = true WHERE `id` = {}"

def getSource(source):
		'''Get corresponding marketing source ID for a source'''
		return {
			'Bus': 225,
			'Recommended by a friend': 8,
			'Search Engine (Google)': 7,
			'Other': 2,
			'Facebook': 152,
			'London Underground (Tube)': 280,
			'Magazine': 19,
		}.get(source, 335)

if SYNC_ENABLED:
	### Connecting to Mediweight DB
	connectionString = 'DRIVER={MySQL};SERVER=127.0.0.1;DATABASE=mediweight;UID=root;PWD=e5uhin54ju84hg'
	connection = pyodbc.connect(connectionString)
	cursor = connection.cursor()

	mw_db = pd.read_sql(READ_FULL_QUERY, connection)
	mw_filtered_db = pd.read_sql(READ_FILTERED_QUERY, connection)

	# An instance of eclinic logger
	logger = eclinic_logger.Logger()

	for idx, row in mw_filtered_db.iterrows():
		alreadyExported = len(mw_db[(mw_db.email == row['email']) & (mw_db.exported_eclinic == 1)])
		if not alreadyExported:
			name = ' '.join(row['name'].split()).split(maxsplit=1)
			nameFirst =  name[0] if len(name) > 0 else ''
			nameLast = name[1] if len(name) > 1 else ''
			email = row['email']
			phone = row['phone']
			marketingSource = getSource(row['source'])
			nhsNumber = '' if row['subscribe'] == 1 else 'Mediweight Unsubcribed'
			dateOfEnquiry = row['submissiontime'].strftime('%Y-%m-%d')

			patient = Patient()
			patient.setFirstName(nameFirst)
			patient.setLastName(nameLast)
			patient.setPhoneMobile(phone)
			patient.setEmail(email)
			patient.setMarketingSourceId(marketingSource)
			patient.setMarketingCategoryId(1)
			patient.setActive(True)
			patient.setTreatmentGroupId(146)
			patient.setTreatmentTypeId(1168)
			patient.setDateOfEnquiry(dateOfEnquiry)
			patient.setNhsNumber(nhsNumber)

			data = patient.getPatientData()

			logger.info('Pushing entry {} to eclinic'.format(row['id']))
			try:
				res = requests.post(url=API_ENDPOINT, headers=HEADERS, json=data)
				logger.info('Entry {} has been pushed'.format(row['id']))
			except Exception as e:
				logger.error(str(e))

			cursor.execute(RECORD_UPDATE_QUERY.format(row['id']))
			# Ensure that the changes would get implemented
			connection.commit()
	connection.close()
