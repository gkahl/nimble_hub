for x in range(row):
        valid = 0
        edge1 = -1
        edge2 = -1
        valid_e1 = 1
        valid_ez1 = 0
        valid_ez2 = 0
        valid_e2 = 1
        skip = 10
        for y in range(col-30):
            if(skip>0):
                skip = skip - 1
                continue
            pixel = [None] * 30
            for i in range(30):
                pixel[i] = depth_array[x,y+i]

            if(abs(pixel[0] - pixel[1]) >= err):
                if(valid == 0):
                    for i in range(29):
                        if(abs(pixel[0] - pixel[1+i])< err):
                            valid_e1 = 0
                        if(pixel[1+i] > .009):
                            valid_ez1 = 1
                    if(valid_e1 == 1):
                        if(valid_ez1 == 1):
                            edge1 = y
                            valid = 1
                    if(valid_e1 == 0):
                        valid_e1=1
                        valid_ez1=0
                        skip = 30
                    if(valid_ez1 == 0):
                        valid_ez1 = 1
                        skip = 30
                if(valid):
                    for i in range(29):
                        if(abs(pixel[0] - pixel[1+i])< err):
                            valid_e2 = 0
                        if(pixel[1+i] > .009):
                            valid_ez2 = 1
                    if(valid_e2 == 1):
                        if(valid_ez2 == 1):
                            edge2 = y
                            valid = 1
                    if(valid_e2 == 0):
                        valid_e2=1
                        skip = 30
                    if(valid_ez2 == 0):
                        valid_ez2 = 1
                        skip = 30for x in range(row):
        valid = 0
        edge1 = -1
        edge2 = -1
        valid_e1 = 1
        valid_ez1 = 0
        valid_ez2 = 0
        valid_e2 = 1
        skip = 10
        for y in range(col-30):
            if(skip>0):
                skip = skip - 1
                continue
            pixel = [None] * 30
            for i in range(30):
                pixel[i] = depth_array[x,y+i]

            if(abs(pixel[0] - pixel[1]) >= err):
                if(valid == 0):
                    for i in range(29):
                        if(abs(pixel[0] - pixel[1+i])< err):
                            valid_e1 = 0
                        if(pixel[1+i] > .009):
                            valid_ez1 = 1
                    if(valid_e1 == 1):
                        if(valid_ez1 == 1):
                            edge1 = y
                            valid = 1
                    if(valid_e1 == 0):
                        valid_e1=1
                        valid_ez1=0
                        skip = 30
                    if(valid_ez1 == 0):
                        valid_ez1 = 1
                        skip = 30
                if(valid):
                    for i in range(29):
                        if(abs(pixel[0] - pixel[1+i])< err):
                            valid_e2 = 0
                        if(pixel[1+i] > .009):
                            valid_ez2 = 1
                    if(valid_e2 == 1):
                        if(valid_ez2 == 1):
                            edge2 = y
                            valid = 1
                    if(valid_e2 == 0):
                        valid_e2=1
                        skip = 30
                    if(valid_ez2 == 0):
                        valid_ez2 = 1
                        skip = 30