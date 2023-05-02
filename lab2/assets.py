from dagster import asset, get_dagster_logger
import pandas as pd

@asset(description="The purpose of this asset is to show off the logger capability by logging information.")
def print_with_info():
    # Get our Logger
    logger = get_dagster_logger()
    # Log out general information
    logger.info('This is how you use the information logger')
    # Create a dummy dataframe
    df = pd.DataFrame({'column1': [1,2,3], 'column2': [4,5,6]})

    ##########################################################
    ################# Insert Code Below ######################
    ##########################################################
    

@asset(description="The purpose of this asset is to show off the logger capability with warnings")
def print_with_warning():
    # Get our Logger
    logger = get_dagster_logger()
    # Log out warning information
    logger.warn('This is how you use the warning logger')
    # Create a dummy dataframe
    df = pd.DataFrame({'column1': [1,2,3], 'column2': [4,5,6]})

    ##########################################################
    ################# Insert Code Below ######################
    ##########################################################


@asset(description="The purpose of this asset is to show off the logger capability with warnings")
def print_with_error():
    # Get our Logger
    logger = get_dagster_logger()
    # Log out general information
    logger.error('This is how you use the error logger')
    # Create a dummy dataframe
    df = pd.DataFrame({'column1': [1,2,3], 'column2': [4,5,6]})

    ##########################################################
    ################# Insert Code Below ######################
    ##########################################################


@asset(description="The purpose of this asset is to show off the logger capability with warnings")
def print_with_critical_error():
    # Get our Logger
    logger = get_dagster_logger()
    # Log out critical errors
    logger.critical('This is how you use the critical error logger')
    # Create a dummy dataframe
    df = pd.DataFrame({'column1': [1,2,3], 'column2': [4,5,6]})

    ##########################################################
    ################# Insert Code Below ######################
    ##########################################################
    
