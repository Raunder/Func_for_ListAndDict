def check_headers_and_value(main_table: list[list[dict]]) ->  bool:
    try:
            data = {}
            header_of_main_table = main_table[0][0].keys()
            for key in header_of_main_table:
                data[f'{key}'] = type(main_table[0][0][key])
            for step, table in enumerate(main_table):
                for idx, item in enumerate(main_table[step]):
                    for key in data:
                        if [*item] != [*header_of_main_table]:
                            print("\033[33mINFO: Re-write headers of data\033[0m")
                            return False
                        if type(main_table[step][idx][key]) != data[key]:
                            print("\033[33mINFO: Re-write type of data\033[0m")
                            return False
            return True
    except:
        print("\033[41mERROR: ValueError\033[0m")
        return False



def union(*args: list[dict],  keys_check: bool = True) -> list[dict]:
    try:
        main_table = []
        for idx, item in enumerate(args):
            if len(args[idx]) != 0 :
                main_table.append(args[idx])
        if len(main_table) == 0  :
            return main_table

    except:
        print("\033[33mINFO: Empty data\033[0m")
        raise ValueError

    if keys_check :
        entry_flag = check_headers_and_value(main_table)
        if not entry_flag:
            raise ValueError("\033[41mERROR: ValueError\033[0m")

    try:
        union_table = []
        for step, table in enumerate(main_table):
            for idx, item in enumerate(main_table[step]):
                if item not in union_table: union_table.append(item)
        return union_table

    except:
        return print("\033[41mERROR: Re-write data correctly\033[0m")


def intersection(*args: list[dict], keys_check: bool = True) -> list[dict]:
    try:
        main_table = []
        for idx, item in enumerate(args):
            if len(args[idx]) != 0 :
                main_table.append(args[idx])
        if len(main_table) == 0  :
            return main_table

    except:
        print("\033[33mINFO: Empty data\033[0m")
        raise ValueError

    if keys_check :
        entry_flag = check_headers_and_value(main_table)
        if not entry_flag:
            raise ValueError("\033[41mERROR: ValueError\033[0m")

    try:
        intersection_table = []
        for item in args[0]:
            for idx, table in enumerate(args[1:]):
                if item in table and item not in intersection_table: intersection_table.append(item)
                elif item not in table and item in intersection_table: intersection_table.remove(item)
        return intersection_table

    except:
        raise ValueError("\033[41mERROR: Re-write data correctly\033[0m")


def difference(*args: list[dict], keys_check: bool = True) -> list[dict]:
    # Check lens of agr's
    try:
        main_table = []
        for idx, item in enumerate(args):
            if len(args[idx]) != 0 :
                main_table.append(args[idx])
        if len(main_table) == 0  :
            return main_table

    except:
        print("\033[33mINFO: Empty data\033[0m")
        raise ValueError

    # Flag check
    if keys_check :
        entry_flag = check_headers_and_value(main_table)
        if not entry_flag:
            raise ValueError("\033[41mERROR: ValueError\033[0m")

    try:
        difference_table = [*args[0]]
        for item in args[0]:
            for idx, table in enumerate(args[1:]):
                if item in table and item in difference_table: difference_table.remove(item)
        difference_table_unique = []
        [difference_table_unique.append(item) for item in difference_table if item not in difference_table_unique]  # Remove duplicates
        return difference_table_unique

    except:
        raise ValueError("\033[41mERROR: Re-write data correctly\033[0m")

