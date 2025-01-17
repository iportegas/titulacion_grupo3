category_lista=['entertainment', 'food_dining', 'gas_transport', 'grocery_net', 'grocery_pos', 
 'health_fitness', 'home', 'kids_pets', 'misc_net', 'misc_pos', 'personal_care', 
 'shopping_net', 'shopping_pos', 'travel']

city_lista=[
    'Albuquerque', 'Altonah', 'Alva', 'American Fork', 'Angwin', 'Arnold', 'Arvada',
    'Ashford', 'Athena', 'Aurora', 'Azusa', 'Ballwin', 'Bay City', 'Blairsden-Graeagle',
    'Blairstown', 'Brainard', 'Brashear', 'Broomfield', 'Browning', 'Buellton', 
    'Burbank', 'Burlington', 'Camden', 'Campbell', 'Cardwell', 'Carlotta', 
    'Carroll', 'Cascade Locks', 'Centerview', 'Claremont', 'Clarksville', 
    'Colorado Springs', 'Colton', 'Conway', 'Corona', 'Coulee Dam', 'Craig', 
    'Crownpoint', 'Daly City', 'Downey', 'Dumont', 'Espanola', 'Eugene', 
    'Fiddletown', 'Fields Landing', 'Fort Washakie', 'Freedom', 'Fullerton', 
    'Gardiner', 'Glendale', 'Greenview', 'Grenada', 'Hatch', 'Hawthorne', 'Helm', 
    'High Rolls Mountain Park', 'Holstein', 'Honokaa', 'Hooper', 'Howells', 
    'Hubbell', 'Humboldt', 'Huntington Beach', 'Huslia', 'Iliff', 'Independence', 
    'Indian Wells', 'Issaquah', 'Jelm', 'Jordan Valley', 'June Lake', 'Kaktovik', 
    'Kansas City', 'Kent', 'Kirk', 'Kirtland', 'Kirtland Afb', 'Kissee Mills', 
    'La Grande', 'Lagrange', 'Laguna Hills', 'Lake Oswego', 'Lakeport', 'Lamy', 
    'Laramie', 'Littleton', 'Llano', 'Lonetree', 'Los Angeles', 'Louisiana', 
    'Loving', 'Lowell', 'Luray', 'Malad City', 'Manley', 'Manville', 'Matthews', 
    'Meadville', 'Mendon', 'Meredith', 'Meridian', 'Mesa', 'Moab', 'Monitor', 
    'Moriarty', 'Mound City', 'Mountain Center', 'Napa', 'Nelson', 'Newberg', 
    'Newhall', 'North Loup', 'Norwalk', 'Oakland', 'Odessa', 'Omaha', 'Orient', 
    'Owensville', 'Paauilo', 'Palmdale', 'Paradise Valley', 'Parker', 'Parker Dam', 
    'Parks', 'Phoenix', 'Pleasant Hill', 'Port Costa', 'Portland', 'Powell Butte', 
    'Pueblo', 'Ravenna', 'Red Cliff', 'Red River', 'Redford', 'Riverton', 
    'Rock Springs', 'Rocky Mount', 'Roseland', 'Ruidoso', 'Sacramento', 
    'Saint Louis', 'San Diego', 'San Jose', 'Santa Monica', 'Scotts Mills', 
    'Seattle', 'Seligman', 'Shedd', 'Sixes', 'Smith River', 'Spirit Lake', 
    'Sprague', 'Stayton', 'Sun City', 'Superior', 'Sutherland', 'Syracuse', 
    'Tekoa', 'Thompson', 'Tomales', 'Unionville', 'Utica', 'Vacaville', 
    'Valentine', 'Vancouver', 'Vinton', 'Wales', 'Wappapello', 'Weeping Water', 
    'Wendel', 'Westerville', 'Westfir', 'Wheaton', 'Williamsburg', 'Woods Cross', 
    'Yellowstone National Park'
]


state_lista= [
    'Alaska', 'Arizona', 'California', 'Colorado', 'Hawaii', 'Idaho', 
    'Missouri', 'Nebraska', 'New Mexico', 'Oregon', 'Utah', 
    'Washington', 'Wyoming'
]

profession_lista= [
    'Administradores', 'Arte', 'Educación', 'Ejecutivos', 
    'Ingeniería y Técnicos', 'Other', 'Salud'
]

state_city_dicts={'New Mexico': ['Loving', 'Llano', 'Kirtland Afb', 'Espanola', 'Albuquerque', 'Red River', 'Lamy', 'Kirtland',
                 'Ruidoso', 'Crownpoint', 'Moriarty', 'High Rolls Mountain Park'],'Washington': ['Burlington','Ashford', 'Monitor', 
                 'Conway', 'Vancouver', 'Issaquah', 'Seattle', 'Burbank', 'Tekoa', 'Colton', 'Coulee Dam', 'Orient'], 
                 'Oregon': ['Eugene', 'Shedd', 'Kent', 'Jordan Valley', 'Sixes', 'Gardiner', 'Powell Butte', 'Athena', 'Lowell', 
                 'Bay City', 'Westfir', 'Cascade Locks', 'Scotts Mills', 'Stayton', 'La Grande', 'Newberg', 'Lake Oswego', 'Portland'], 
                 'Missouri': ['Saint Louis', 'Pleasant Hill', 'Utica', 'Seligman', 'Kansas City', 'Mound City', 'Redford', 'Syracuse', 
                 'Centerview', 'Wappapello', 'Clarksville', 'Rocky Mount', 'Unionville', 'Louisiana', 'Owensville', 'Blairstown', 'Odessa', 
                 'Independence', 'Browning', 'Cardwell', 'Luray', 'Brashear', 'Meadville', 'Ballwin', 'Kissee Mills', 'Matthews', 'Arnold', 
                 'Wheaton', 'Williamsburg', 'Camden'], 'California': ['Tomales', 'Port Costa', 'San Diego', 'Grenada', 'Wendel', 'Glendale', 
                 'San Jose', 'Vacaville', 'Mountain Center', 'Napa', 'Greenview', 'Fiddletown', 'Huntington Beach', 'Parker Dam', 
                 'Laguna Hills', 'Sacramento', 'Hawthorne', 'Sun City', 'June Lake', 'Downey', 'Helm', 'Carlotta', 'Corona', 'Claremont', 
                 'Buellton', 'Santa Monica', 'Oakland', 'Los Angeles', 'Newhall', 'Norwalk', 'Palmdale', 'Daly City', 'Indian Wells', 
                 'Smith River', 'Azusa', 'Blairsden-Graeagle', 'Angwin', 'Vinton', 'Fields Landing', 'Lakeport'], 
                 'Arizona': ['Humboldt', 'Paradise Valley', 'Phoenix', 'Superior', 'Parks', 'Mesa'], 
                 'Colorado': ['Aurora', 'Dumont', 'Kirk', 'Pueblo', 'Broomfield', 'Littleton', 'Arvada', 'Parker', 'Red Cliff', 
                 'Meredith', 'Colorado Springs', 'Iliff'], 'Nebraska': ['Brainard', 'Weeping Water', 'Valentine', 'Omaha', 'Howells', 
                 'Sutherland', 'Campbell', 'Hooper', 'Sprague', 'Manley', 'Holstein', 'Carroll', 'Westerville', 'Nelson', 'North Loup', 
                 'Roseland', 'Ravenna', 'Fullerton', 'Hubbell'], 'Utah': ['Moab', 'Thompson', 'American Fork', 'Mendon', 'Woods Cross', 
                 'Hatch', 'Altonah'], 'Idaho': ['Meridian', 'Spirit Lake', 'Malad City', 'Mesa'], 
                 'Wyoming': ['Lagrange', 'Lonetree', 'Freedom', 'Rock Springs', 'Manville', 'Yellowstone National Park', 'Riverton', 
                 'Laramie', 'Fort Washakie', 'Jelm', 'Alva'], 
                 'Hawaii': ['Paauilo', 'Honokaa'], 'Alaska': ['Wales', 'Kaktovik', 'Huslia', 'Craig']}

state_city_dict = {state: sorted(cities) for state, cities in sorted(state_city_dicts.items())}