import csv

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """    
    list_of_dict=[]
    with open(filename,'r') as csv_file:
        csv_reader=csv.DictReader(csv_file,delimiter=separator,quotechar=quote)
        for line in csv_reader:
            list_of_dict.append(line)
            
    return list_of_dict


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    
    dict_of_values = {}
    with open(filename, newline='') as csv_file:
        reader = csv.DictReader(csv_file,
                                delimiter=separator,
                                quotechar=quote)
        for row in reader:
            temp_dict = {}
            for name in row:
                temp_dict[name] = row[name]
            dict_of_values[row[keyfield]] = temp_dict
            
    return dict_of_values



MINIMUM_AB = 500

def batting_average(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the batting average as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return hits / at_bats
    else:
        return 0

def onbase_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the on-base percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    walks = float(batting_stats[info["walks"]])
    if at_bats >= MINIMUM_AB:
        return (hits + walks) / (at_bats + walks)
    else:
        return 0

def slugging_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the slugging percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    doubles = float(batting_stats[info["doubles"]])
    triples = float(batting_stats[info["triples"]])
    home_runs = float(batting_stats[info["homeruns"]])
    singles = hits - doubles - triples - home_runs
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return (singles + 2 * doubles + 3 * triples + 4 * home_runs) / at_bats
    else:
        return 0




def filter_by_year(statistics, year, yearid):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      year       - Year to filter by
      yearid     - Year ID field in statistics
    Outputs:
      Returns a list of batting statistics dictionaries that
      are from the input year.
    """
    statistics_for_yearid = []
    for value in statistics:
        if yearid in value:
            if int(value.get(yearid)) == year:
                statistics_for_yearid.append(value)
    return statistics_for_yearid
    

def top_player_ids(info, statistics, formula, numplayers):
    """
    Inputs:
      info       - Baseball data information dictionary
      statistics - List of batting statistics dictionaries
      formula    - function that takes an info dictionary and a
                   batting statistics dictionary as input and
                   computes a compound statistic
      numplayers - Number of top players to return
    Outputs:
      Returns a list of tuples, player ID and compound statistic
      computed by formula, of the top numplayers players sorted in
      decreasing order of the computed statistic.
    """

    top_players = []
    top_players_list = []
    
    for values in statistics:
        key = "".join(values[info["playerid"]])
        value = formula(info,values)
        top_players.append((key, value))

    for _ in range(numplayers):
        max_val, max_player = 0, ""
        for player in top_players:
            if player[1] > max_val and player not in top_players_list:
                max_val = player[1]
                max_player = player[0]
        top_players_list.append((max_player, max_val))
    return top_players_list


def lookup_player_names(info, top_ids_and_stats):
    """
    Inputs:
      info              - Baseball data information dictionary
      top_ids_and_stats - list of tuples containing player IDs and
                          computed statistics
    Outputs:
      List of strings of the form "x.xxx --- FirstName LastName",
      where "x.xxx" is a string conversion of the float stat in
      the input and "FirstName LastName" is the name of the player
      corresponding to the player ID in the input.
    """
    with open(info["masterfile"], newline='') as csvfile:
        reader = csv.DictReader(csvfile,
                                delimiter=info["separator"],
                                quotechar=info["quote"])
        
        player_names, player_info = {}, []

        for player in reader:
            player_names[player[info["playerid"]]] = (player[info["firstname"]], 
                                                      player[info["lastname"]])

        for top_id in top_ids_and_stats:
            player_info.append("{:0.3f} --- {} {}".format(top_id[1], 
                                                          player_names[top_id[0]][0],
                                                          player_names[top_id[0]][1]))
        return player_info


def compute_top_stats_year(info, formula, numplayers, year):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
      year        - Year to filter by
    Outputs:
      Returns a list of strings for the top numplayers in the given year
      according to the given formula.
    """
    with open(info["battingfile"], newline='') as csvfile:
        reader = csv.DictReader(csvfile,
                                delimiter=info["separator"],
                                quotechar=info["quote"])
        
        stats = filter_by_year(reader, year, info['yearid'])
        
        return lookup_player_names(info, top_player_ids(info, stats, formula, numplayers))



def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      playerid   - Player ID field name
      fields     - List of fields to aggregate
    Output:
      Returns a nested dictionary whose keys are player IDs and whose values
      are dictionaries of aggregated stats.  Only the fields from the fields
      input will be aggregated in the aggregated stats dictionaries.
    """

    aggregated_players = {}

    for stat in statistics:
        if stat[playerid] in aggregated_players:
            for field in fields:
                if field in aggregated_players[stat[playerid]]:
                    aggregated_players[stat[playerid]][field] += int(stat[field])
        else: 
            temp_dict = {}           
            for field in fields:                
                temp_dict[playerid] = stat[playerid]
                temp_dict[field] = int(stat[field])
            aggregated_players[stat[playerid]] = temp_dict
            
    return aggregated_players


def compute_top_stats_career(info, formula, numplayers):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
    """
    
    
    with open(info["battingfile"], newline='') as csvfile:
        reader = csv.DictReader(csvfile,
                                delimiter=info["separator"],
                                quotechar=info["quote"])        
      
        stats = aggregate_by_player_id(reader, info["playerid"], info["battingfields"])
        
        stat_list = [stats[stat] for stat in stats]
            
        return lookup_player_names(info, top_player_ids(info, stat_list, formula, numplayers))




def test_baseball_statistics():

    ''' Dictionary contains informations needed to access baseball statistics'''
    ''' This information is all tied to the format and contents of the CSV files'''
    
    baseballdatainfo = {"masterfile": "Master_2016.csv",   
                        "battingfile": "Batting_2016.csv", 
                        "separator": ",",                  
                        "quote": '"',                      
                        "playerid": "playerID",            
                        "firstname": "nameFirst",          
                        "lastname": "nameLast",            
                        "yearid": "yearID",                
                        "atbats": "AB",                    
                        "hits": "H",                       
                        "doubles": "2B",                   
                        "triples": "3B",                  
                        "homeruns": "HR",                  
                        "walks": "BB",                     
                        "battingfields": ["AB", "H", "2B", "3B", "HR", "BB"]}

    print("Top 5 batting averages in 1923")
    top_batting_average_1923 = compute_top_stats_year(baseballdatainfo, batting_average, 5, 1923)
    for player in top_batting_average_1923:
        print(player)
    print("")

    print("Top 10 batting averages in 2010")
    top_batting_average_2010 = compute_top_stats_year(baseballdatainfo, batting_average, 10, 2010)
    for player in top_batting_average_2010:
        print(player)
    print("")

    print("Top 10 on-base percentage in 2010")
    top_onbase_2010 = compute_top_stats_year(baseballdatainfo, onbase_percentage, 10, 2010)
    for player in top_onbase_2010:
        print(player)
    print("")

    print("Top 10 slugging percentage in 2010")
    top_slugging_2010 = compute_top_stats_year(baseballdatainfo, slugging_percentage, 10, 2010)
    for player in top_slugging_2010:
        print(player)
    print("")

    print("Top 10 OPS in 2010")
    top_ops_2010 = compute_top_stats_year(baseballdatainfo,
                                          lambda info, stats: (onbase_percentage(info, stats) +
                                                               slugging_percentage(info, stats)),
                                          10, 2010)
    for player in top_ops_2010:
        print(player)
    print("")

    print("Top 20 career batting averages")
    top_batting_average_career = compute_top_stats_career(baseballdatainfo, batting_average, 20)
    for player in top_batting_average_career:
        print(player)
    print("")


