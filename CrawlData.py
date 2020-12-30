from bs4 import BeautifulSoup
import requests

class Craw():
    def Craw_data_from_web(self):


        url = 'https://www.worldometers.info/coronavirus/country/us/'

        page = requests.get(url, verify=False)

        soup = BeautifulSoup(page.text, features="html.parser")

        # look for the id 'usa_table_countries_yesterday
        all_states = soup.find_all('table', id="usa_table_countries_yesterday")

        content = bytes(str(all_states[0]).replace('\n', ''),
                    'utf8')  # convert the string into byte representation, #strip all of the new lines in the string

        soup = BeautifulSoup(content, features="html.parser")

        fixed_list = []
        final_list = soup.find_all('td')  # find all of the <td> elements within the table

        for i in final_list[:len(final_list) - 96]:
            if '[' not in i.text and i.text.strip() != '':
                fixed_list.append(i.text)
            else:  # replace anything that has an empty space with '0'
                fixed_list.append('0')

        state_stats = []
        state_object = {}
        counter = 0
        current_state = ''  # keep track of the current state that is being proccessed

        for state in fixed_list:
            if counter == 1:
                current_state = state.strip()
            elif counter in [2, 3, 4, 5, 6, 10]: # Just get some nessessary data like total case, death, new case.
                state_stats.append(state)
            elif counter == 13:
                state_stats.append(state)
                state_object[current_state] = state_stats[:-1]
                state_stats = []
                counter = 0
                continue
            counter = counter + 1
        return (state_object) # the dictionary of key with the data
