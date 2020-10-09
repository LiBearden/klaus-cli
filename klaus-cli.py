import click
import requests
import json
__author__ = "Elliot Bearden"

# Establish authentication constants
ACCOUNT_ID = input("Please enter your account ID:")
CONNECTION_TOKEN = input("Please enter your connection token:")


# Instantiate "export" click command group
@click.group()
def main():
    """
    An elementary CLI for exporting data from workspaces hosted on the Klaus app
    """
    pass


# Instantiate "export" command, with "--date-range" option (work in progress)
@main.command()
@click.option('--date_range', help='Date range that you would like to pull data from.')
@click.argument('workspace_id', nargs=1)
def export(workspace_id, date_range=None):
    """This command captures the date range of the data that you would like to export. """
    r = requests.get(
        "https://kibbles.klausapp.com/api/v1/payment/{acc_id}/workspace/{w_id}/reviews".format(acc_id=ACCOUNT_ID, w_id=workspace_id),
        headers={"Authorization": "Bearer {token}".format(token=CONNECTION_TOKEN)},
        params={"fromDate": "2020-10-02T04:02:24.327Z",
                "toDate": "2020-10-09T04:02:24.327Z"
                })
    response_bytes = r.content
    response_data = response_bytes.decode('utf-8').replace("'", '"')
    print('-' * 20)
    response_string = json.loads(response_data)
    response_json = json.dumps(response_string, indent=4)
    print(response_json)


# Call main function to start CLI
if __name__ == "__main__":
    main()