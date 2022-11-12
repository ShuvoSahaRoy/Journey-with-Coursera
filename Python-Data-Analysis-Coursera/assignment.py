import csv


def read_csv_as_list_dict(filename, separator, quote):
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator,
                                   quotechar=quote)
        list_dict = []
        for row in list(csvreader):
            list_dict.append(row)
    return list_dict


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator,
                                   quotechar=quote)
        dic_dict = {}
        for row in csvreader:
            dic_dict[row[keyfield]] = row
    return dic_dict


MINIMUM_AB = 500


def batting_average(baseball_info, batting_stats):
    hits= float(batting_stats[baseball_info["hits"]])
    at_bats= float(batting_stats[baseball_info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return hits/at_bats
    else:
        return 0


def onbase_percentage(baseball_info, batting_stats):
    hits = float(batting_stats[baseball_info["hits"]])
    at_bats = float(batting_stats[baseball_info["atbats"]])
    walks = float(batting_stats[baseball_info["walks"]])
    if at_bats >= MINIMUM_AB:
        return (hits+walks)/(at_bats+walks)
    else:
        return 0


def slugging_percentage(baseball_info, batting_stats):
    hits = float(batting_stats[baseball_info["hits"]])
    at_bats = float(batting_stats[baseball_info["atbats"]])
    walks = float(batting_stats[baseball_info["walks"]])
    doubles = float(batting_stats[baseball_info["doubles"]])
    triples = float(batting_stats[baseball_info["triples"]])
    home_runs = float(batting_stats[baseball_info["home_runs"]])
    singles = hits - doubles - triples - home_runs
    if at_bats >= MINIMUM_AB:
        return (singles + 2 * doubles + 3 * triples + 4 * home_runs) / at_bats
    else:
        return 0


def filter_by_year(statistics, year, yearid):
    new_list = []
    for row in statistics:
        if int(row[yearid]) == year:
            new_list.append(row)
    return new_list


def top_player_ids(info, statistics, formula, numplayers):
    new_list = []
    final_list = []
    for row in statistics:
        player_id = row[info['playerid']]
        comp_stat = formula(info,statistics)
        current_tuple = tuple((player_id, comp_stat))
        new_list.append(current_tuple)

    new_list.sort(key=lambda x: x[1], reverse=True)
    for tup_index in new_list:
        if numplayers>0:
            final_list.append(tuple(tup_index))
            numplayers -=1
        else:
            break
    return final_list


def lookup_player_names(info, top_ids_and_stats):
    new_list = []
    info_dict = read_csv_as_nested_dict(info['masterfile'], info['playerid'], info['separator'], info['quote'])
    for idx in top_ids_and_stats:
        formatted_string = format(idx[1], '.3f') + " --- {0} {1}".format(info_dict[idx[0]][info['firstname']],
                                                                         info_dict[idx[0]][info['lastname']])
        new_list.append(formatted_string)
    return new_list


def compute_top_stats_year(info, formula, numplayers, year):
    stats_list = read_csv_as_list_dict(info['battingfile'],
                                       info['separator'],
                                       info['quote']
                                       )
    # filter by year using filter_by_year()
    filtered_by_year = filter_by_year(stats_list,
                                      year,
                                      info['yearid'])
    # return list of tuples of top players using top_player_ids()
    top_players = top_player_ids(info, filtered_by_year, formula, numplayers)
    # return list of strings for top numplayers using
    return lookup_player_names(info, top_players)

def aggregate_by_player_id(statistics, playerid, fields):
    final_dict = {}
    stats_dict = {}

    for row in statistics:

        # 1 the first time you see a player, create a new entry in final_dict
        if row[playerid] not in final_dict:
            # add the playerid to the nested dictionary
            stats_dict[playerid] = row[playerid]
            # for each stat to aggregate in fields, add the stat to the nested dictionary
            for field in fields:
                stats_dict[field] = int(row[field])
            # remember to add the dict in 'dict(stats_dict)' so that
            # the stats_dict fields will not get overwritten
            final_dict[row[playerid]] = dict(stats_dict)
        # 2 if the player is already in final_dict
        else:
            # for each stat to aggregate in fields, update the stat
            for field in fields:
                final_dict[row[playerid]][field] += int(row[field])

    return final_dict

def compute_top_stats_career(info, formula, numplayers):
    stats = []
    # aggregate the stats for each player so that you are operating on career statistics
    aggregated_stats = aggregate_by_player_id(
        read_csv_as_list_dict(info['battingfile'], info['separator'], info['quote']),
        info['playerid'],
        info['battingfields'])

    # add each dictionary row in agreggated_stats to the stats list
    # to have an easily usable stats list to pass to other functions
    for value in aggregated_stats.values():
        stats.append(value)
    # use lookup_player_names and top_player_ids to return top players
    return lookup_player_names(info, top_player_ids(info, stats, formula, numplayers))