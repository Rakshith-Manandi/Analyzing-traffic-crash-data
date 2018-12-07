def preprocess_person_killed_by_age():
    '''
    preprocess age file for visualization

    :returns: 
    :return type: lists
    
    '''
    import pandas as pd
    
    line1 = [] # <20
    line2 = [] # 21~44
    line3 = [] # 45~64
    line4 = [] # >65
    total = []
    
    years = [str(i) for i in list(range(1994,2017))]
    
    for i in range(1994,2017):
        df = pd.read_csv(r'data/Number of fatalities by age group (1994~2016)/%d.xls'%(i),sep = '\t',header = None)
        df = df.iloc[1:,:]
        df.columns = ['age', 'number','nan']
        num = df['number']
        line1.append(sum(map(int,num[0:4])))
        line2.append(sum(map(int,num[4:7])))
        line3.append(sum(map(int,num[7:9])))
        line4.append(sum(map(int,num[9:11])))
        total.append(int(num[13]))
    return years, line1, line2, line3, line4, total



def preprocess_rural_and_urban(fname):
    '''
    read in the file 'speed' and preprocess it

    :param fname: filename for source text
    :type fname: str

    :returns: 
    :return type: lists
    
    '''
    import pandas as pd
    from bokeh.models import ColumnDataSource
    
    assert isinstance(fname,str)
    df = pd.read_csv( fname, sep = '\t', header = None)
    df = df.iloc[3:,:]
    df.columns = ['speed', 'rural1','rural2','urban1','urban2','uk1','uk2','total','nan','nan']
    speed = list(df['speed'][:5])
    rural = list(df['rural1'][:5])
    urban = list(df['urban1'][:5])
    data = {'speed' : speed,
            'rural': rural,
           'urban': urban}

    source = ColumnDataSource(data=data)
    
    return speed, data, source


def person_killed_by_type(fname):
    '''
    read in the file 'person type' and preprocess it

    :param fname: filename for source text
    :type fname: str

    :returns: 
    :return type: lists
    
    '''
    import pandas as pd
    
    assert isinstance(fname,str)
    df = pd.read_csv( fname ,sep = '\t',header = None)
    df = df.iloc[3:,:]
    df.columns = ['year', 'cars','t1','t2','motor','bus','uk1','total1','p1','p2','uk2','nonmotor','nan','total','nan']
    years = list(range(1994,2017))
    motor = list(map(int,df['motor']))
    cars = list(map(int,df['cars']))
    t1 = list(df['t1'])
    t2 = list(df['t2'])
    trucks = [int(t1[i]) + int(t2[i]) for i in range(len(t1))]
    nonmotor = list(map(int,df['nonmotor']))
    total = list(map(int,df['total']))
    return years, cars, trucks, motor, nonmotor, total



def preprocess_ratio_of_fatalities_by_years():
    '''
    Output ratio of fatalities per million people by years

    :returns: 
    :return type: lists
    
    '''
    import numpy as np

    #population along the years
    populations = np.array([323128,320897,318563,316205,313998,311663,309348,306772,304094,301231,298380,295517,292805,290108,287625,284969,
                   282162,272691,270248,267784,265229,262803,260327])

    #fatalities along the years
    fatalities = np.array([37461,35485,32744,32893,33782,32479,32999,33883,37423,41259,42708,43510,42836,
                          42884,43005,42196,41945,41717,41501,42013,42065,41817,40716])
    #crashes along the years
    crashes = np.array([34748,32539,30056,30202,31006,29867,30296,30862,34172,37435,38648,39252,
               38444,38477,38491,37862,37526,37140,37107,37324,37494,37241,36254])

    years = list(range(1994,2017))
    years.reverse()
    fat = fatalities/(populations/1000)
    crash = crashes/(populations/1000)
    
    return years, fat, crash
