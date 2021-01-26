def all_the_same(elements):
    for element in elements:
        i = element
        try: 
            if not i == j:
                return False
        except:
            pass
        j = element
    return True
