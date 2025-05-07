# Details our Database spreadsheet which has details of all files, ID in Transport Department

Database_File_spreadsheet_ID = gc.open_by_key('1nJKyvV1WQmZzvbjOP7Hsp1bQJmiNsYoJOH_jIL7H9PI') #ID of Database Spreadsheet
MASsheetID = Database_File_spreadsheet_ID.worksheet('MAS')                                    #MAS Worksheet
OdometersheetID = Database_File_spreadsheet_ID.worksheet('Odometer')                          #Odometer Worksheet

#STS RR SVP
RR_Oil_Lub_Coolant_DEF_spreadsheet_id = MASsheetID.acell('C2').value                  # Get the spreadsheet ID from cell C2
RR_Oil_Lub = gc.open_by_key(RR_Oil_Lub_Coolant_DEF_spreadsheet_id)                    # Open RR_Oil_Lub spreadsheet

RR_Engine_oil_CH_BSIV_worksheet_name = MASsheetID.acell('B2').value                        # Get the worksheet name from cell B2
engine_oil_CH_BSIV_CH_MAS_rr = RR_Oil_Lub.worksheet(RR_Engine_oil_CH_BSIV_worksheet_name)  # Open RR CH engineoil worksheet

RR_Engine_oil_CK_BSVI_worksheet_name = MASsheetID.acell('B3').value                        # Get the worksheet name from cell B3
engine_oil_CK_BSVI_CK_MAS_rr = RR_Oil_Lub.worksheet(RR_Engine_oil_CK_BSVI_worksheet_name)  # Open RR CK engineoil worksheet

RR_Report1_worksheet_name = MASsheetID.acell('B8').value                                # Get the worksheet name from report1, RR Km between and after last servicing
RR_Report1_Worksheet = RR_Oil_Lub.worksheet(RR_Report1_worksheet_name)                  # Open RR Km between and after last servicing worksheet

#STS ATR SVP
ATR_Oil_Lub_Coolant_DEF_spreadsheet_id = MASsheetID.acell('C52').value                  # Get the spreadsheet ID from cell C51 ATR
ATR_Oil_Lub = gc.open_by_key(ATR_Oil_Lub_Coolant_DEF_spreadsheet_id)                    # Open ATR_Oil_Lub spreadsheet

ATR_Engine_oil_CH_BSIV_worksheet_name = MASsheetID.acell('B52').value                         # Get the worksheet name from cell B52
engine_oil_CH_BSIV_CH_MAS_ATR = ATR_Oil_Lub.worksheet(ATR_Engine_oil_CH_BSIV_worksheet_name)  # Open ATR CH engineoil worksheet

ATR_Engine_oil_CK_BSVI_worksheet_name = MASsheetID.acell('B53').value                         # Get the worksheet name from cell B52
engine_oil_CK_BSVI_CK_MAS_ATR = ATR_Oil_Lub.worksheet(ATR_Engine_oil_CK_BSVI_worksheet_name)  # Open ATR CK engineoil worksheet

#ATR_Report1_worksheet_name = MASsheetID.acell('B58').value                           #******This may not be required       # Get the worksheet name from report1, RR Km between and after last servicing
#ATR_Report1_Worksheet = ATR_Oil_Lub.worksheet(ATR_Report1_worksheet_name)              #This may not be required     # Open RR Km between and after last servicing worksheet

#STS FG
FG_Oil_Lub_Coolant_DEF_spreadsheet_id = MASsheetID.acell('C102').value                  # Get the spreadsheet ID from cell C51 ATR
FG_Oil_Lub = gc.open_by_key(FG_Oil_Lub_Coolant_DEF_spreadsheet_id)                    # Open ATR_Oil_Lub spreadsheet

FG_Engine_oil_CH_BSIV_worksheet_name = MASsheetID.acell('B102').value                         # Get the worksheet name from cell B2
engine_oil_CH_BSIV_CH_MAS_FG = FG_Oil_Lub.worksheet(FG_Engine_oil_CH_BSIV_worksheet_name)  # Open RR engineoil worksheet

#FG_Report1_worksheet_name = MASsheetID.acell('B108').value                    #*****This may not be required            # Get the worksheet name from report1, RR Km between and after last servicing
#FG_Report1_Worksheet = FG_Oil_Lub.worksheet(FG_Report1_worksheet_name)          #This may not be required         # Open RR Km between and after last servicing worksheet

