import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and path to your service account key JSON file
SCOPE = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'C:/Users/lmyhe/Desktop/Code_Academy/API/service_account.json.json'

def get_data():
    # Authorize using the service account credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPE)
    gc = gspread.authorize(credentials)

    # Open the spreadsheet
    sheet = gc.open_by_key('1ToJbRUsRrrHi0LMBNfLVB00QOoIdRpt_IOXPS6KvJSE') 
    worksheet = sheet.get_worksheet(0)

    # Get all values from the sheet
    values = worksheet.get_all_values()

    return values

# Call the function to get the data
spreadsheet_data = get_data()

# Convert the data to a DataFrame
df = pd.DataFrame(spreadsheet_data[1:], columns=spreadsheet_data[0])

# Print the DataFrame
print(df)

# Draw line chart
st.write('Line Chart')
chart = alt.Chart(df).mark_line().encode(
    x='dt',
    y='temp'
).interactive()
st.altair_chart(chart, use_container_width=True)
