class Settings:
    """
    Default properties
    """

    USERNAME = "<username>"
    PASSWORD = "<password>"
    PRIVATE_AREA = "https://www.uniecampus.it/area-riservata"
    SIGNIN_BUTTON_NAME = "_eventId_proceed"
    GO_TO_PAGE_ONE = "https://www.uniecampus.it/area-riservata/lezioni-e-laboratori"
    GO_TO_PAGE_TWO = (
        "https://www.uniecampus.it/area-riservata/lezioni-e-laboratori/vai-a-studiare"
    )
    FRAME_NAME = "iframe"
    FIRST_PART_OF_NAME = "ctl00_ContentPlaceHolder1_d_dettaglio_ctl0"
    END_PART_OF_NAME = "_button1"
    ELEMENT_NAME = "ctl00_ContentPlaceHolder1_b_prossima"
    ELEMENT_BY_X_PATH = "//table[@id='ctl00_ContentPlaceHolder1_d_dettaglio']/tbody/tr"
    ERROR_BOTTOM = "ctl00_ContentPlaceHolder1_pbOkErrScorm"


settings = Settings()
