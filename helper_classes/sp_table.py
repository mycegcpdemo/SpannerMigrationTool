class SpannerTable:

    table = """CREATE TABLE LISTINGS (
              id INT64 NOT NULL,
              TIMESTAMP_created DATE,
              TIMESTAMP_upDATEd DATE,
              ListingMLS STRING(255) NOT NULL,
              ListingPrice INT64,
              ListingPriceOld INT64,
              ListingPriceChanged DATE,
              ListingPriceOrig INT64,
              ListingLastPrice INT64,
              ListingPricelow INT64,
              ListingHOAFee1 FLOAT64,
              ListingHOAFee2 FLOAT64,
              HasHOA STRING(255),
              ListingType STRING(255),
              ListingSubType STRING(255),
              ListingStyle STRING(255),
              ListingStatus STRING(255),
              ListingStatusOld STRING(255),
              ListingStatusChanged DATE,
              ListingRemarks STRING(255),
              ListingImage STRING(255),
              ListingDATE DATE,
              PendingDATE DATE,
              ListingModificationDATE DATE,
              ListingPriceDATE DATE,
              StatusChangeDATE DATE,
              CloseDATE DATE,
              ClosePrice INT64,
              DescriptionFinancing STRING(255),
              DescriptionSoldTerms STRING(255),
              SaleAgentID STRING(255),
              SaleAgent STRING(255),
              SaleCoAgentID STRING(255),
              SaleCoAgent STRING(255),
              SaleOfficeID STRING(255),
              SaleOffice STRING(255),
              ListingDOM INT64,
              ListingLeaseTermTime STRING(255),
              ListingLeaseLength INT64,
              Address STRING(255),
              AddressArea STRING(255),
              AddressSubdivision STRING(255),
              AddressCity STRING(255),
              AddressCounty STRING(255),
              AddressState STRING(255),
              AddressZipCode STRING(255),
              AddressStreetNumber STRING(255),
              AddressStreetName STRING(255),
              AddressStreetType STRING(255),
              AddressStreetDirPrefix STRING(255),
              AddressStreetDirSuffix STRING(255),
              SchoolDistrict STRING(255),
              SchoolElementary STRING(255),
              SchoolMiddle STRING(255),
              SchoolHigh STRING(255),
              NumberOfBedrooms INT64,
              NumberOfBathrooms FLOAT64,
              NumberOfBathsFull INT64,
              NumberOfBathsHalf INT64,
              NumberOfSqFt INT64,
              NumberOfSqFtLot INT64,
              NumberOfAcres FLOAT64,
              NumberOfStories INT64,
              NumberOfGarages INT64,
              NumberOfParkingSpaces INT64,
              NumberOfFireplaces INT64,
              YearBuilt INT64,
              HasSpa STRING(255),
              HasView STRING(255),
              HasPool STRING(255),
              HasFireplace STRING(255),
              HasBasement STRING(255),
              IsWaterfront STRING(255),
              IsForeclosure STRING(255),
              IsShortSale STRING(255),
              IsBankOwned STRING(255),
              IsRangePrice STRING(255),
              IsConsiderLease STRING(255),
              IsCreditReportRequired STRING(255),
              IsVariableRate STRING(255),
              IsOceanfront STRING(255),
              IsBeachfront STRING(255),
              IsWaterView STRING(255),
              IsOceanView STRING(255),
              IsPierView STRING(255),
              IsWhiteWaterView STRING(255),
              IsPanoramicView STRING(255),
              IsCoastlineView STRING(255),
              LotLocation STRING(255),
              DescriptionLot STRING(255),
              DescriptionLotSize STRING(255),
              DescriptionSqFt STRING(255),
              DescriptionPool STRING(255),
              DescriptionView STRING(255),
              DescriptionStories STRING(255),
              DescriptionFireplace STRING(255),
              DescriptionWaterfront STRING(255),
              DescriptionBasement STRING(255),
              DescriptionGarages STRING(255),
              DescriptionParking STRING(255),
              DescriptionAmenities STRING(255),
              DescriptionAppliances STRING(255),
              DescriptionUtilities STRING(255),
              DescriptionFeatures STRING(255),
              DescriptionExterior STRING(255),
              DescriptionExteriorFeatures STRING(255),
              DescriptionInterior STRING(255),
              DescriptionInteriorFeatures STRING(255),
              DescriptionRooms STRING(255),
              DescriptionHeating STRING(255),
              DescriptionCooling STRING(255),
              DescriptionZoning STRING(255),
              DescriptionRoofing STRING(255),
              DescriptionWindows STRING(255),
              DescriptionConstruction STRING(255),
              DescriptionFoundation STRING(255),
              DescriptionHOAFees STRING(255),
              DescriptionHOAFeesFrequency STRING(255),
              DescriptionCommonWalls STRING(255),
              DescriptionSqFtSource STRING(255),
              DescriptionLotSizeSource STRING(255),
              DescriptionHandicap STRING(255),
              DescriptionDoors STRING(255),
              DescriptionTaxMelloRoos STRING(255),
              DescriptionAssociationAmenities STRING(255),
              DescriptionOtherAssociationFees STRING(255),
              DescriptionHOAFeeFrequency1 STRING(255),
              DescriptionHOAFeeFrequency2 STRING(255),
              DescriptionListingTerms STRING(255),
              DescriptionSpa STRING(255),
              DescriptionSecurity STRING(255),
              DescriptionFloors STRING(255),
              DescriptionCreditReportPaidBy STRING(255),
              DescriptionFurnished STRING(255),
              DescriptionPetsAllowed STRING(255),
              DescriptionSurvey STRING(255),
              DescriptionElectric STRING(255),
              DescriptionGas STRING(255),
              DescriptionAssessments STRING(255),
              DescriptionLegalDisclosures STRING(255),
              DescriptionAssociationFeesInclude STRING(255),
              DescriptionSpecial STRING(255),
              DescriptionLocation STRING(255),
              BuildersTractCode STRING(255),
              BuildersTractName STRING(255),
              BuildersName STRING(255),
              LandLeaseAmount INT64,
              LandLeaseAmountPerYear INT64,
              SellingOfficeCompensation FLOAT64,
              DepositPet FLOAT64,
              DepositOther FLOAT64,
              DepositSecurity FLOAT64,
              CreditReportAmount INT64,
              NumberOfUnits INT64,
              GrossScheduledIncome FLOAT64,
              GrossOperatingIncome FLOAT64,
              ExpenseOperating FLOAT64,
              NumberOfBuildings INT64,
              OtherStructures STRING(255),
              ExpenseActualAnnualVacancy FLOAT64,
              TaxNew FLOAT64,
              ExpenseInsurance FLOAT64,
              ActualAnnualGrossRent FLOAT64,
              MonthlyGrossIncome FLOAT64,
              ActualGrossAnnualIncome FLOAT64,
              Inclusions STRING(255),
              PricePerUnit INT64,
              UnitNumber STRING(255),
              UnitFurnished01 STRING(255),
              UnitMonthlyRent01 FLOAT64,
              UnitNumberOfBath01 FLOAT64,
              UnitNumberOfBed01 INT64,
              UnitTotalMonthlyRent01 FLOAT64,
              UnitFurnished02 STRING(255),
              UnitMonthlyRent02 FLOAT64,
              UnitNumberOfBath02 FLOAT64,
              UnitNumberOfBed02 INT64,
              UnitTotalMonthlyRent02 FLOAT64,
              UnitFurnished03 STRING(255),
              UnitMonthlyRent03 FLOAT64,
              UnitNumberOfBath03 FLOAT64,
              UnitNumberOfBed03 INT64,
              UnitTotalMonthlyRent03 FLOAT64,
              UnitFurnished04 STRING(255),
              UnitMonthlyRent04 FLOAT64,
              UnitNumberOfBath04 FLOAT64,
              UnitNumberOfBed04 INT64,
              UnitTotalMonthlyRent04 FLOAT64,
              UnitFurnished05 STRING(255),
              UnitMonthlyRent05 FLOAT64,
              UnitNumberOfBath05 FLOAT64,
              UnitNumberOfBed05 INT64,
              UnitTotalMonthlyRent05 FLOAT64,
              UnitFurnished06 STRING(255),
              UnitMonthlyRent06 FLOAT64,
              UnitNumberOfBath06 FLOAT64,
              UnitNumberOfBed06 INT64,
              UnitTotalMonthlyRent06 FLOAT64,
              UnitFurnished07 STRING(255),
              UnitMonthlyRent07 FLOAT64,
              UnitNumberOfBath07 FLOAT64,
              UnitNumberOfBed07 INT64,
              UnitTotalMonthlyRent07 FLOAT64,
              UnitFurnished08 STRING(255),
              UnitMonthlyRent08 FLOAT64,
              UnitNumberOfBath08 FLOAT64,
              UnitNumberOfBed08 INT64,
              UnitTotalMonthlyRent08 FLOAT64,
              UnitFurnished09 STRING(255),
              UnitMonthlyRent09 FLOAT64,
              UnitNumberOfBath09 FLOAT64,
              UnitNumberOfBed09 INT64,
              UnitTotalMonthlyRent09 FLOAT64,
              UnitFurnished10 STRING(255),
              UnitMonthlyRent10 FLOAT64,
              UnitNumberOfBath10 FLOAT64,
              UnitNumberOfBed10 INT64,
              UnitTotalMonthlyRent10 FLOAT64,
              UnitFurnished11 STRING(255),
              UnitMonthlyRent11 FLOAT64,
              UnitNumberOfBath11 FLOAT64,
              UnitNumberOfBed11 INT64,
              UnitTotalMonthlyRent11 FLOAT64,
              UnitFurnished12 STRING(255),
              UnitMonthlyRent12 FLOAT64,
              UnitNumberOfBath12 FLOAT64,
              UnitNumberOfBed12 INT64,
              UnitTotalMonthlyRent12 FLOAT64,
              UnitFurnished13 STRING(255),
              UnitMonthlyRent13 FLOAT64,
              UnitNumberOfBath13 FLOAT64,
              UnitNumberOfBed13 INT64,
              UnitTotalMonthlyRent13 FLOAT64,
              OpenHouseTime STRING(255),
              OpenHouseDATE DATE,
              OpenHouseRefreshments STRING(255),
              OpenHouseRemarks STRING(255),
              OpenHouseAgent STRING(255),
              OpenHouseAgentID STRING(255),
              OpenHouseType STRING(255),
              OpenHouseEnd STRING(255),
              OpenHouseStart STRING(255),
              OpenHouseTime2 STRING(255),
              OpenHouseDATE2 DATE,
              OpenHouseRefreshments2 STRING(255),
              OpenHouseRemarks2 STRING(255),
              OpenHouseAgent2 STRING(255),
              OpenHouseAgentID2 STRING(255),
              OpenHouseType2 STRING(255),
              OpenHouseEnd2 STRING(255),
              OpenHouseStart2 STRING(255),
              OpenHouseTime3 STRING(255),
              OpenHouseDATE3 DATE,
              OpenHouseRefreshments3 STRING(255),
              OpenHouseRemarks3 STRING(255),
              OpenHouseAgent3 STRING(255),
              OpenHouseAgentID3 STRING(255),
              OpenHouseType3 STRING(255),
              OpenHouseEnd3 STRING(255),
              OpenHouseStart3 STRING(255),
              OpenHouseTime4 STRING(255),
              OpenHouseDATE4 DATE,
              OpenHouseRefreshments4 STRING(255),
              OpenHouseRemarks4 STRING(255),
              OpenHouseAgent4 STRING(255),
              OpenHouseAgentID4 STRING(255),
              OpenHouseType4 STRING(255),
              OpenHouseEnd4 STRING(255),
              OpenHouseStart4 STRING(255),
              ListingOffice STRING(255),
              ListingOfficeID STRING(255),
              ListingCoOffice STRING(255),
              ListingCoOfficeID STRING(255),
              ListOfficePhone STRING(255),
              ListOfficePhoneExt STRING(255),
              ListingAgent STRING(255),
              ListingAgentID STRING(255),
              ListAgentCellPhone STRING(255),
              ListAgentDirectPhone STRING(255),
              ListAgentDirectPhoneExt STRING(255),
              ListAgentPreferredPhone STRING(255),
              ListAgentPreferredPhoneExt STRING(255),
              ListAgentEmail STRING(255),
              ListingCoAgent STRING(255),
              ListingCoAgentID STRING(255),
              TaxParcelNumber STRING(255),
              PropertyCondition STRING(255),
              LandLeaseDescription STRING(255),
              Latitude FLOAT64,
              Longitude FLOAT64,
              VirtualTour STRING(255),
              Senior STRING(255),
              DescriptionAttached STRING(255),
              OCFirst INT64,
            ) PRIMARY KEY(id)
            """
