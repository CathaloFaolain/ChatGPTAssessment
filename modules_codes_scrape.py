import requests
from bs4 import BeautifulSoup
import pandas as pd

# list of school codes used in requests
schools = [ # "S142", # School of Agriculture and Food Science
            # "S003", # School of Archaeology
            "S143",  # School of Architecture, Planning and Environmental Policy
            # "S005", # School of Art History and Cultural Policy
            # "S006", # School of Biology and Environmental Science
            # "S007", # School of Biomolecular and Biomedical Science
            "S144",  # School of Biosystems and Food Engineering
            # "S008", # School of Business
            "S009",  # School of Chemical and Bioprocess Engineering
            # "S010", # School of Chemistry
            "S145",  # School of Civil Engineering
            # "S011", # School of Classics
            # "S012", # School of Computer Science
            # "S018", # School of Earth Sciences
            # "S013", # School of Economics
            # "S014", # School of Education
            "S146",  # School of Electrical and Electronic Engineering
            # "S016", # School of English, Drama and Film
            # "S017", # School of Geography
            # "S019", # School of History
            # "S020", # School of Information and Communication Studies
            # "S021", # School of Irish, Celtic Studies and Folklore
            # "S022", # School of Languages, Cultures and Linguistics
            # "S023", # School of Law
            # "S024", # School of Mathematics and Statistics
            "S147"  ########## ADD IN COMMA IF INCLUDING SCHOOLS BELOW#, # School of Mechanical and Materials Engineering
            # "S025", # School of Medicine
            # "S026", # School of Music
            # "S027", # School of Nursing, Midwifery and Health Systems
            # "S028", # School of Philosophy
            # "S029", # School of Physics
            # "S031", # School of Politics and International Relations
            # "S032", # School of Psychology
            # "S137", # School of Public Health, Physiotherapy and Sports Science
            # "S171", # School of Social Policy, Social Work and Social Justice
            # "S035", # School of Sociology
            # "S148", # School of Veterinary Medicine
            # "S042", # Applied Language Centre
            # "S165", # Beijing Dublin International College (BDIC)
            # "S173", # Central Office - College of Health and Agricultural Sciences
            # "S039", # Central Office - College of Social Sciences and Law
            # "S184", # Chang’an-Dublin International College of Transportation (CDIC)
            # "S041", # Clinton Institute for American Studies
            # "S036", # College of Arts and Humanities Adm
            # "S150", # College of Engineering and Architecture Administration Office
            # "S151", # College of Science Administration Office
            # "S045", # Conway Institute of Biomolecular and Biomedical Research
            # "S185", # Guangzhou-Dublin International College of Life Sciences and Technology (GDIC)
            # "S157", # Innovation Academy
            # "S155", # Institute of Bankers
            # "S108", # Irish Institute for Chinese Studies
            # "S134", # Teaching and Learning
            # "S062"  # UCD Global
            ]

# for each school named above, obtain modules based in each school
for s in schools:
    url = "https://hub.ucd.ie/usis/W_HU_REPORTING.P_DISPLAY_QUERY?p_code1=ALL&p_code2="+s+"&p_query=CB216-1&p_parameters=" # url of page containing all modules based in school s
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    tags = []  # use to store tags found when parsing through returned request
    mod_list = {}  # dict used to store module codes/names
    # in the returned request, modules are listed as hyperlinks <a>, so search using this tag
    for element in soup.select('a'):
        tags.append(element.text)
    # all hyperlinks from the page are returned - find only module hyperlinks
    start = tags.index("Help")  # Help always comes before first module
    end = tags.index("PDF")  # PDF always comes after last module
    for t in range(start+1, end-2):
        # remove items from list that are not modules
        if tags[t] == "See Video" or tags[t] == "See sample lesson":
            del tags[t]
        x = tags[t].split(" - ")  # separate module code and name
        # do not include modules ending in a letter - not based in Ireland
        # store modules in dictionary
        if x[0][-1].isnumeric() == True:
            mod_list[x[0]] = x[1]
        else:
            continue
    # convert dictionary to data frame and save dataframe as csv
    df = pd.DataFrame.from_dict(mod_list, orient="index")
    df.to_csv(s+".csv")

