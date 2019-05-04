import numpy as np
import pandas as pd
import taxcalc as tc


def cash_income(df):
    """Calculates income after taxes and cash transfers.

    Defined as aftertax_income minus non-cash benefits.

    Args:
        df: A Tax-Calculator pandas DataFrame with columns for
            * aftertax_income
            * snap_ben
            * 
    
    Returns:
        A pandas Series with the cash income for each row in df.
    """
    return (df.aftertax_income -
            (1 - tc.HOUSING_CASH_SHARE) * df.housing_ben -
            (1 - tc.MCAID_CASH_SHARE) * df.mcaid_ben -
            (1 - tc.MCARE_CASH_SHARE) * df.mcare_ben -
            (1 - tc.OTHER_CASH_SHARE) * df.other_ben -
            (1 - tc.SNAP_CASH_SHARE) * df.snap_ben -
            (1 - tc.SSI_CASH_SHARE) * df.ssi_ben -
            (1 - tc.TANF_CASH_SHARE) * df.tanf_ben -
            (1 - tc.VET_CASH_SHARE) * df.vet_ben -
            (1 - tc.WIC_CASH_SHARE) * df.wic_ben)