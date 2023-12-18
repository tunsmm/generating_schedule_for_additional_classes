import os
import numpy as np
import pandas as pd


class GroupsClassesParser:
    def __init__(self):
        self.schedules = []
    
    def _findStart(self, dataframe):
        bool_rename = False
        idx = 0
        new_df = pd.DataFrame()

        for i in range(len(dataframe[0])):
            if dataframe[0][i].lower() == "сентябрь":
                idx = i
                break
            if dataframe[0][i].upper() == "ПОНЕДЕЛЬНИК":
                idx = i - 1
                bool_rename = True
                break

        if bool_rename:
            new_df = dataframe.rename(columns={4: 'error', 0: 4})[idx:-3]
        else:
            new_df = dataframe[idx:-3]

        return new_df
    
    def _modifyXSLX(self, name):
        df2 = pd.read_excel(name, header=None, keep_default_na=False)
        df2 = self._findStart(df2)
        df2 = df2[:-2]

        df2 = df2.replace(['NaN'], None)
        df2 = df2.dropna(how='all')

        dofes = np.array(df2[4]).astype('str')
        dofes = np.char.upper(dofes)

        where_mon = np.where(dofes == "ПОНЕДЕЛЬНИК")
        evens_odds = np.zeros(len(df2))
        evens_odds = np.where(evens_odds == 0.0, None, 1)
        evens_odds[where_mon[0][0]] = "НЕЧЕТНАЯ"
        evens_odds[where_mon[0][1]] = "ЧЕТНАЯ"
        df2['evens_odds'] = evens_odds

        df2 = df2.replace([''], None)
        df2.reset_index(drop=True, inplace=True)
        df2[4] = df2[4].fillna(method='ffill')
        df2[5] = df2[5].fillna(method='ffill')
        df2['evens_odds'] = df2['evens_odds'].fillna(method='ffill')

        groups = df2.iloc[[0]]
        groups = groups.dropna(axis=1, how='all')
        groups = np.array(groups)
        groups = groups[0][4:]

        first_str = df2.iloc[[0]]

        df_without_head = df2[1:]
        df_without_head = df_without_head.dropna(subset=[5])
        df_without_head.reset_index(drop=True, inplace=True)
        df_without_head = df_without_head.replace([None], 'None')

        for i in range(6, df_without_head.shape[1]-1, 4):
            df_without_head.loc[(df_without_head[i] != 'None'), i] = "NOTFOUND"

        for i in range(6+3, df_without_head.shape[1]-1, 4):
            df_without_head.loc[(df_without_head[i] != 'None'), i] = "END"

        for i in range(6+3, df_without_head.shape[1]-1, 4):
            for j in range(0, len(df_without_head[9])):
                if df_without_head[i][j] == "END":
                    if j-2 <= 0:
                        continue
                    if df_without_head[i-3][j-2] == "NOTFOUND":
                        df_without_head.loc[j-2:j, i-3:i] = "FOUND"

        for i in range(6+3, df_without_head.shape[1]-1, 4):
            for j in range(0, len(df_without_head[9])):
                if df_without_head[i][j] == "END":
                    if j-5 <= 0:
                        continue
                    if df_without_head[i-3][j-5] == "NOTFOUND":
                        df_without_head.loc[j-5:j, i-3:i] = "FOUND"

        for i in range(6+3, df_without_head.shape[1]-1, 4):
            for j in range(0, len(df_without_head[9])):
                if df_without_head[i][j] == "END":
                    for k in range(7, 7+4*20, 4):
                        if i-k < 0:
                            continue
                        if j-2 <= 0:
                            continue
                        if df_without_head[i-k][j-2] == "NOTFOUND":
                            df_without_head.loc[j-2:j, i-k:i] = "FOUND"
                            break
        for i in range(6, df_without_head.shape[1]-3, 4):
            for j in range(0, len(df_without_head[9])):
                if df_without_head[i][j] == "NOTFOUND":
                    if i+3 >= df_without_head.shape[1]-3:
                        df_without_head.loc[j:j, i:i] = "FOUND"
                        continue
                    if df_without_head[i+3][j] == "END":
                        if j-2 <= 0:
                            continue
                        df_without_head.loc[j-2:j, i:i+3] = "FOUND"
                    elif i+7 < df_without_head.shape[1]-3:
                        if df_without_head[i+7][j] == "END":
                            if j-5 <= 0:
                                continue
                            df_without_head.loc[j-5:j, i:i+7] = "FOUND"

        for i in range(6, df_without_head.shape[1]-3, 4):
            for j in range(0, len(df_without_head[9])):
                if df_without_head[i][j] == "NOTFOUND":
                    df_without_head.loc[j:j, i:i+3] = "FOUND"

        for i in range(6, df_without_head.shape[1]-2, 4):
            del df_without_head[i+1]
            del df_without_head[i+2]

            try:
                del df_without_head[i+3]
            except:
                print("EXCEPT WITH" + name) 

        b = df_without_head[5]
        a = []
        for i in b:
            a.append(int(i.split('-')[-1].replace(' ', '')) // 2)
        cnt = 1
        cur = -1
        to_delete = []

        for i, v in enumerate(a):
            if v == cur:
                cnt += 1
                if cnt > 3:
                    to_delete.append(i)
            else:
                cnt = 1
                cur = v

        df_without_head[5] = a
        df_without_head = df_without_head.drop(labels=to_delete, axis=0)
        df_without_head.reset_index(drop=True, inplace=True)
        df_without_head = df_without_head.replace(['None'], '')

        result = df_without_head.groupby(np.arange(len(df_without_head))//3).max()
        return result, groups
    
    def getJson(self, path):
        """
        Данный метод получает на вход путь к папке, в которой лежат расписания.
        :param path: путь к папке, в которой лежат расписания.
        :return: файл, который содержит в себе список групп, для каждой выписаны свободные и занятые пары.
        """
        schedules_list = []
        rez = os.listdir(path)
        for n, item in enumerate(rez):
            filename = path / item
            schedules_list.append(filename)
        
        self.schedules = schedules_list
        modified_xslxs = []
        all_groups = []
        for filename in self.schedules:
            result, groups = self._modifyXSLX(filename)
            modified_xslxs.append(result)
            all_groups.append(groups)
        
        weekdays = modified_xslxs[0][4].unique()
        evens = modified_xslxs[0]['evens_odds'].unique()
        classes = modified_xslxs[0][5].unique()
        free = []
        for even in evens:
            for weekday in weekdays:
                for class_ in classes:
                    free.append({"weekday": weekday, "even": even, "class": str(class_)})
        free = np.array(free)
        
        my_json = []
        for idx, result in enumerate(modified_xslxs):
            groups_indices = list(result.columns)[2:-1]
            for i in range(len(all_groups[idx])):
                group_free = np.copy(free).tolist()
                group_busy = []
                for j in range(0, len(result[groups_indices[i]])):
                    if result[groups_indices[i]][j] == "FOUND":
                        busy_classday = {'weekday': result[4][j].upper(), 'even': result['evens_odds'][j],
                                         'class': str(result[5][j])}
                        group_busy.append(busy_classday)
                        try:
                            group_free.remove(busy_classday)
                        except:
                            print("EXCEPT IN " + all_groups[idx][i])
                grop_df = {"name": all_groups[idx][i], "free_classes": group_free, "busy_classes": group_busy}
                grop_df_2 = {"group": grop_df}
                my_json.append(grop_df_2)
        
        return my_json
      
