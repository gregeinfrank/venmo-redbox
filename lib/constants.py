DB_NAME = 'venmo_redbox'
DB_USER = 'root'
DB_PASSWORD = 'venmo'

HELP_TEXT = """
usage: venmo_redbox.py <who|rent|steal> <box-name>

who:  Displays who currently owns box-name, if it is taken.

rent: Rents the box if it is available ( also gives option to steal )

steal: Rents the box even if it is not available.  Don't be a jerk!  Limit 
       the usage of 'steal'

"""
