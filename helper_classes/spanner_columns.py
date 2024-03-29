class SpannerColumns:
    columns = (
        'id', 'TIMESTAMP_created', 'TIMESTAMP_upDATEd', 'ListingMLS', 'ListingPrice', 'ListingPriceOld',
        'ListingPriceChanged',
        'ListingPriceOrig', 'ListingLastPrice', 'ListingPricelow', 'ListingHOAFee1', 'ListingHOAFee2', 'HasHOA',
        'ListingType',
        'ListingSubType', 'ListingStyle', 'ListingStatus', 'ListingStatusOld', 'ListingStatusChanged', 'ListingRemarks',
        'ListingImage', 'ListingDATE', 'PendingDATE', 'ListingModificationDATE', 'ListingPriceDATE', 'StatusChangeDATE',
        'CloseDATE', 'ClosePrice', 'DescriptionFinancing', 'DescriptionSoldTerms', 'SaleAgentID', 'SaleAgent',
        'SaleCoAgentID',
        'SaleCoAgent', 'SaleOfficeID', 'SaleOffice', 'ListingDOM', 'ListingLeaseTermTime', 'ListingLeaseLength',
        'Address',
        'AddressArea', 'AddressSubdivision', 'AddressCity', 'AddressCounty', 'AddressState', 'AddressZipCode',
        'AddressStreetNumber', 'AddressStreetName', 'AddressStreetType', 'AddressStreetDirPrefix',
        'AddressStreetDirSuffix',
        'SchoolDistrict', 'SchoolElementary', 'SchoolMiddle', 'SchoolHigh', 'NumberOfBedrooms', 'NumberOfBathrooms',
        'NumberOfBathsFull', 'NumberOfBathsHalf', 'NumberOfSqFt', 'NumberOfSqFtLot', 'NumberOfAcres', 'NumberOfStories',
        'NumberOfGarages', 'NumberOfParkingSpaces', 'NumberOfFireplaces', 'YearBuilt', 'HasSpa', 'HasView', 'HasPool',
        'HasFireplace', 'HasBasement', 'IsWaterfront', 'IsForeclosure', 'IsShortSale', 'IsBankOwned', 'IsRangePrice',
        'IsConsiderLease', 'IsCreditReportRequired', 'IsVariableRate', 'IsOceanfront', 'IsBeachfront', 'IsWaterView',
        'IsOceanView', 'IsPierView', 'IsWhiteWaterView', 'IsPanoramicView', 'IsCoastlineView', 'LotLocation',
        'DescriptionLot',
        'DescriptionLotSize', 'DescriptionSqFt', 'DescriptionPool', 'DescriptionView', 'DescriptionStories',
        'DescriptionFireplace', 'DescriptionWaterfront', 'DescriptionBasement', 'DescriptionGarages',
        'DescriptionParking',
        'DescriptionAmenities', 'DescriptionAppliances', 'DescriptionUtilities', 'DescriptionFeatures',
        'DescriptionExterior',
        'DescriptionExteriorFeatures', 'DescriptionInterior', 'DescriptionInteriorFeatures', 'DescriptionRooms',
        'DescriptionHeating', 'DescriptionCooling', 'DescriptionZoning', 'DescriptionRoofing', 'DescriptionWindows',
        'DescriptionConstruction', 'DescriptionFoundation', 'DescriptionHOAFees', 'DescriptionHOAFeesFrequency',
        'DescriptionCommonWalls', 'DescriptionSqFtSource', 'DescriptionLotSizeSource', 'DescriptionHandicap',
        'DescriptionDoors', 'DescriptionTaxMelloRoos', 'DescriptionAssociationAmenities',
        'DescriptionOtherAssociationFees',
        'DescriptionHOAFeeFrequency1', 'DescriptionHOAFeeFrequency2', 'DescriptionListingTerms', 'DescriptionSpa',
        'DescriptionSecurity', 'DescriptionFloors', 'DescriptionCreditReportPaidBy', 'DescriptionFurnished',
        'DescriptionPetsAllowed', 'DescriptionSurvey', 'DescriptionElectric', 'DescriptionGas',
        'DescriptionAssessments',
        'DescriptionLegalDisclosures', 'DescriptionAssociationFeesInclude', 'DescriptionSpecial', 'DescriptionLocation',
        'BuildersTractCode', 'BuildersTractName', 'BuildersName', 'LandLeaseAmount', 'LandLeaseAmountPerYear',
        'SellingOfficeCompensation', 'DepositPet', 'DepositOther', 'DepositSecurity', 'CreditReportAmount',
        'NumberOfUnits',
        'GrossScheduledIncome', 'GrossOperatingIncome', 'ExpenseOperating', 'NumberOfBuildings', 'OtherStructures',
        'ExpenseActualAnnualVacancy', 'TaxNew', 'ExpenseInsurance', 'ActualAnnualGrossRent', 'MonthlyGrossIncome',
        'ActualGrossAnnualIncome', 'Inclusions', 'PricePerUnit', 'UnitNumber', 'UnitFurnished01', 'UnitMonthlyRent01',
        'UnitNumberOfBath01', 'UnitNumberOfBed01', 'UnitTotalMonthlyRent01', 'UnitFurnished02', 'UnitMonthlyRent02',
        'UnitNumberOfBath02', 'UnitNumberOfBed02', 'UnitTotalMonthlyRent02', 'UnitFurnished03', 'UnitMonthlyRent03',
        'UnitNumberOfBath03', 'UnitNumberOfBed03', 'UnitTotalMonthlyRent03', 'UnitFurnished04', 'UnitMonthlyRent04',
        'UnitNumberOfBath04', 'UnitNumberOfBed04', 'UnitTotalMonthlyRent04', 'UnitFurnished05', 'UnitMonthlyRent05',
        'UnitNumberOfBath05', 'UnitNumberOfBed05', 'UnitTotalMonthlyRent05', 'UnitFurnished06', 'UnitMonthlyRent06',
        'UnitNumberOfBath06', 'UnitNumberOfBed06', 'UnitTotalMonthlyRent06', 'UnitFurnished07', 'UnitMonthlyRent07',
        'UnitNumberOfBath07', 'UnitNumberOfBed07', 'UnitTotalMonthlyRent07', 'UnitFurnished08', 'UnitMonthlyRent08',
        'UnitNumberOfBath08', 'UnitNumberOfBed08', 'UnitTotalMonthlyRent08', 'UnitFurnished09', 'UnitMonthlyRent09',
        'UnitNumberOfBath09', 'UnitNumberOfBed09', 'UnitTotalMonthlyRent09', 'UnitFurnished10', 'UnitMonthlyRent10',
        'UnitNumberOfBath10', 'UnitNumberOfBed10', 'UnitTotalMonthlyRent10', 'UnitFurnished11', 'UnitMonthlyRent11',
        'UnitNumberOfBath11', 'UnitNumberOfBed11', 'UnitTotalMonthlyRent11', 'UnitFurnished12', 'UnitMonthlyRent12',
        'UnitNumberOfBath12', 'UnitNumberOfBed12', 'UnitTotalMonthlyRent12', 'UnitFurnished13', 'UnitMonthlyRent13',
        'UnitNumberOfBath13', 'UnitNumberOfBed13', 'UnitTotalMonthlyRent13', 'OpenHouseTime', 'OpenHouseDATE',
        'OpenHouseRefreshments', 'OpenHouseRemarks', 'OpenHouseAgent', 'OpenHouseAgentID', 'OpenHouseType',
        'OpenHouseEnd',
        'OpenHouseStart', 'OpenHouseTime2', 'OpenHouseDATE2', 'OpenHouseRefreshments2', 'OpenHouseRemarks2',
        'OpenHouseAgent2',
        'OpenHouseAgentID2', 'OpenHouseType2', 'OpenHouseEnd2', 'OpenHouseStart2', 'OpenHouseTime3', 'OpenHouseDATE3',
        'OpenHouseRefreshments3', 'OpenHouseRemarks3', 'OpenHouseAgent3', 'OpenHouseAgentID3', 'OpenHouseType3',
        'OpenHouseEnd3', 'OpenHouseStart3', 'OpenHouseTime4', 'OpenHouseDATE4', 'OpenHouseRefreshments4',
        'OpenHouseRemarks4',
        'OpenHouseAgent4', 'OpenHouseAgentID4', 'OpenHouseType4', 'OpenHouseEnd4', 'OpenHouseStart4', 'ListingOffice',
        'ListingOfficeID', 'ListingCoOffice', 'ListingCoOfficeID', 'ListOfficePhone', 'ListOfficePhoneExt',
        'ListingAgent',
        'ListingAgentID', 'ListAgentCellPhone', 'ListAgentDirectPhone', 'ListAgentDirectPhoneExt',
        'ListAgentPreferredPhone',
        'ListAgentPreferredPhoneExt', 'ListAgentEmail', 'ListingCoAgent', 'ListingCoAgentID', 'TaxParcelNumber',
        'PropertyCondition', 'LandLeaseDescription', 'Latitude', 'Longitude', 'VirtualTour', 'Senior',
        'DescriptionAttached',
        'OCFirst',)
