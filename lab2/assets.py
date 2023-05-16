from dagster import asset, get_dagster_logger
import pandas as pd

# Get our logger
logger = get_dagster_logger()

# Generate our data
df = pd.DataFrame({'column1': [1,2,3], 'column2': [4,5,6]})

@asset(description="The purpose of this asset is to show off the logger capability by logging information.")
def print_with_info():
    logger.info('This is how you use the information logger')

    ##########################################################
    ################# Insert Code Below ######################
    ##########################################################
    

@asset(description="The purpose of this asset is to show off the logger capability with warnings")
def print_with_warning():
    logger.warn('This is how you use the warning logger')

    ##########################################################
    ################# Insert Code Below ######################
    ##########################################################

@asset(description="The purpose of this asset is to show off the logger capability with warnings")
def print_with_error():
    logger.error('This is how you use the error logger')

    ##########################################################
    ################# Insert Code Below ######################
    ##########################################################


@asset(description="The purpose of this asset is to show off the logger capability with warnings")
def print_with_critical_error():
    logger.critical('This is how you use the critical error logger')

    ##########################################################
    ################# Insert Code Below ######################
    ##########################################################
