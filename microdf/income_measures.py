import numpy as np
import pandas as pd
import microdf as mdf

"""See https://docs.google.com/spreadsheets/d/1I-Qe8uD58bLnPkimc9eaPgs4AE7x5FZYmTZwVX_WyT8
   for a comparison of income measures used here."""

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


def tpc_eci(df):
    """Approximates Tax Policy Center's Expanded Cash Income measure.

    Subtracts WIC, housing assistance, veteran's benefits, Medicare, and
    Medicaid from expanded_income. ECI adds income measures not modeled in
    Tax-Calculator, so these are ignored and will create a discrepancy
    compared to TPC's ECI.
   
    Args:
        df: DataFrame with columns from Tax-Calculator.

    Returns:
        pandas Series with TPC's ECI.
    """
    return df.expanded_income - df[mdf.ECI_REMOVE_COLS].sum(axis=1)


def market_income(df):
    """ Approximates CBO's market income concept, which is income
        before social insurance, means-tested transfers, and taxes.

    Args:
        df: DataFrame with expanded_income and benefits.
    
    Returns:
        pandas Series of the same length as df.
    """
    return df.expanded_income - df[mdf.BENS].sum(axis=1)
