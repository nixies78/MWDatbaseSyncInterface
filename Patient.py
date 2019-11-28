class Patient:

	def getNhsNumber(self):
		return self.nhsNumber
	
	def setNhsNumber(self, nhsNumber):
		self.nhsNumber = nhsNumber
	
	def getMarketingCategoryId(self):
		return self.marketingCategoryId
	
	def setMarketingCategoryId(self, marketingCategoryId):
		self.marketingCategoryId = marketingCategoryId
	
	def getFirstName(self):
		return self.firstName
	
	def setFirstName(self, firstName):
		self.firstName = firstName
	
	def getLastName(self):
		return self.lastName
	
	def setLastName(self, lastName):
		self.lastName = lastName
	
	def getEmail(self):
		return self.email
	
	def setEmail(self, email):
		self.email = email
	
	def getPhoneMobile(self):
		return self.phoneMobile
	
	def setPhoneMobile(self, phoneMobile):
		self.phoneMobile = phoneMobile
	
	def getMarketingSourceId(self):
		return self.marketingSourceId
	
	def setMarketingSourceId(self, marketingSourceId):
		self.marketingSourceId = marketingSourceId
	
	def getActive(self):
		return self.active
	
	def setActive(self, active):
		self.active = active

	
	def getDateOfEnquiry(self):
		return self.dateOfEnquiry

	
	def setDateOfEnquiry(self, dateOfEnquiry):
		self.dateOfEnquiry = dateOfEnquiry
	
	def getTreatmentGroupId(self):
		return self.treatmentGroupId
	
	def setTreatmentGroupId(self, treatmentGroupId):
		self.treatmentGroupId = treatmentGroupId

	def getTreatmentTypeId(self):
		return self.treatmentTypeId
	
	def setTreatmentTypeId(self, treatmentTypeId):
		self.treatmentTypeId = treatmentTypeId
	
	def getPatientData(self):
		return {
		'firstName': self.getFirstName(),
		'lastName': self.getLastName(),
		'email': self.getEmail(),
		'phoneMobile': self.getPhoneMobile(),
		'marketingSourceId': self.getMarketingSourceId(),
		'active': self.getActive(),
		'dateOfEnquiry': self.getDateOfEnquiry(),
		'treatmentGroupId': self.getTreatmentGroupId(),
		'treatmentTypeId': self.getTreatmentTypeId(),
		'marketingCategoryId': self.getMarketingCategoryId(),
		'nhsNumber': self.getNhsNumber(),
		}