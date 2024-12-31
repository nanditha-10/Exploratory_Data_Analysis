# Exploratory Data Analysis Results

## Data Overview

None

## Data Summary

### Shape
(200, 15)

### Column Names and Types
None

### Head
   User ID  Area code            Location  Gender   YOB Marital Status      Activity  Budget  Cuisines  Alcohol     Smoker  Food Rating  Service Rating  Overall Rating Often A S
0        1        153  Upper East Side,NY  Female  2006         Single  Professional       3  Japanese     Never     Never            5               4             4.5        No
1        2        123       St. George,NY  Female  1991        Married       Student       3    Indian     Never  Socially            1               1             1.0        No
2        3        122  Upper West Side,NY    Male  1977         Single       Student       5   Seafood     Often     Often            5               5             5.0       Yes
3        4        153  Upper East Side,NY  Female  1956        Married  Professional       5  Japanese     Never  Socially            3               1             2.0        No
4        5        129     Central Park,NY    Male  1997         Single       Student       4  Filipino  Socially     Never            2               4             3.0        No

### Tail
     User ID  Area code            Location  Gender   YOB Marital Status      Activity  Budget  Cuisines Alcohol     Smoker  Food Rating  Service Rating  Overall Rating Often A S
195      196        175       St. George,NY  Female  1982         Single  Professional       4    French    Never  Socially            1               2             1.5        No
196      197        170  Upper West Side,NY  Female  2000        Married       Student       4   Chinese    Never     Often            1               2             1.5        No
197      198        160       St. George,NY  Female  2006         Single  Professional       5  Japanese    Never     Often            5               2             3.5        No
198      199        130       St. George,NY    Male  2002        Married       Student       3  Filipino    Never  Socially            3               2             2.5        No
199      200        140  Upper East Side,NY    Male  2005        Married       Student       4    French    Never     Never            3               2             2.5        No

### Missing Values
User ID           0
Area code         0
Location          0
Gender            0
YOB               0
Marital Status    0
Activity          0
Budget            0
Cuisines          0
Alcohol           0
Smoker            0
Food Rating       0
Service Rating    0
Overall Rating    0
Often A S         0

### Quantiles
                count      mean        std     min      0%       5%     50%      95%      99%    100%     max
User ID         200.0   100.500  57.879185     1.0     1.0    10.95   100.5   190.05   198.01   200.0   200.0
Area code       200.0   141.060  26.130257   101.0   101.0   107.00   135.0   188.20   198.00   199.0   199.0
YOB             200.0  1984.830  16.809339  1955.0  1955.0  1956.95  1987.0  2007.00  2009.00  2009.0  2009.0
Budget          200.0     3.815   1.056578     1.0     1.0     1.95     4.0     5.00     5.00     5.0     5.0
Food Rating     200.0     3.220   1.411226     1.0     1.0     1.00     3.0     5.00     5.00     5.0     5.0
Service Rating  200.0     3.230   1.526022     1.0     1.0     1.00     3.0     5.00     5.00     5.0     5.0
Overall Rating  200.0     3.225   1.079445     1.0     1.0     1.50     3.0     5.00     5.00     5.0     5.0

cat_cols: ['Location', 'Gender', 'Marital Status', 'Activity', 'Cuisines', 'Alcohol ', 'Smoker', 'Often A S', 'Budget', 'Food Rating', 'Service Rating', 'Overall Rating']
num_cols: ['User ID', 'Area code', 'YOB']
cat_but_car: []
## Column Types

Categorical Columns: ['Location', 'Gender', 'Marital Status', 'Activity', 'Cuisines', 'Alcohol ', 'Smoker', 'Often A S', 'Budget', 'Food Rating', 'Service Rating', 'Overall Rating']
Numerical Columns: ['User ID', 'Area code', 'YOB']
Categorical but cardinal columns: []

### Summary for Location

Location
St. George,NY         46
Upper East Side,NY    30
Riverdale,NY          28
Central Park,NY       24
China Town, NY        22
Market City, NY       20
Upper West Side,NY    18
Central Park,ny        8
Market City, MY        2
Cedar Hill, NY         2
Name: count, dtype: int64

### Summary for Gender

Gender
Male      118
Female     82
Name: count, dtype: int64

### Summary for Marital Status

Marital Status
Single      100
Married      86
Divorced     14
Name: count, dtype: int64

### Summary for Activity

Activity
Student         120
Professional     80
Name: count, dtype: int64

### Summary for Cuisines

Cuisines
Japanese    36
Filipino    34
French      34
Indian      32
Chinese     24
Seafood     22
Italian     18
Name: count, dtype: int64

### Summary for Alcohol 

Alcohol 
Never       88
Often       61
Socially    51
Name: count, dtype: int64

### Summary for Smoker

Smoker
Socially    71
Often       70
Never       59
Name: count, dtype: int64

### Summary for Often A S

Often A S
No     174
Yes     26
Name: count, dtype: int64

### Summary for Budget

Budget
4    63
5    62
3    61
1    10
2     4
Name: count, dtype: int64

### Summary for Food Rating

Food Rating
5    53
3    46
2    35
4    35
1    31
Name: count, dtype: int64

### Summary for Service Rating

Service Rating
5    66
2    43
1    35
3    29
4    27
Name: count, dtype: int64

### Summary for Overall Rating

Overall Rating
3.5    35
3.0    34
2.5    32
5.0    29
4.0    26
2.0    21
1.5    11
4.5     6
1.0     6
Name: count, dtype: int64

### Summary for User ID

count    200.000000
mean     100.500000
std       57.879185
min        1.000000
5%        10.950000
10%       20.900000
20%       40.800000
30%       60.700000
40%       80.600000
50%      100.500000
60%      120.400000
70%      140.300000
80%      160.200000
90%      180.100000
95%      190.050000
99%      198.010000
max      200.000000
Name: User ID, dtype: float64

User ID
1      1
138    1
128    1
129    1
130    1
      ..
70     1
71     1
72     1
73     1
200    1
Name: count, Length: 200, dtype: int64

### Summary for Area code

count    200.000000
mean     141.060000
std       26.130257
min      101.000000
5%       107.000000
10%      107.000000
20%      121.800000
30%      123.000000
40%      129.000000
50%      135.000000
60%      153.000000
70%      154.000000
80%      163.600000
90%      179.300000
95%      188.200000
99%      198.000000
max      199.000000
Name: Area code, dtype: float64

Area code
123    24
129    17
153    15
107    15
154    14
       ..
120     1
199     1
102     1
106     1
160     1
Name: count, Length: 65, dtype: int64

### Summary for YOB

count     200.000000
mean     1984.830000
std        16.809339
min      1955.000000
5%       1956.950000
10%      1960.900000
20%      1966.600000
30%      1974.000000
40%      1978.600000
50%      1987.000000
60%      1995.000000
70%      1999.000000
80%      2001.200000
90%      2006.000000
95%      2007.000000
99%      2009.000000
max      2009.000000
Name: YOB, dtype: float64

YOB
1974    12
2006    10
2000    10
2001     8
1998     8
1995     6
1977     6
2002     6
1969     6
2007     6
1956     6
2003     6
2009     6
1989     4
1976     4
2005     4
1981     4
1962     4
1964     4
1955     4
1996     4
1961     4
1985     4
1987     4
1975     4
1999     4
1988     4
1971     4
1959     4
1991     4
1965     4
1963     4
1990     2
1960     2
1978     2
1979     2
1994     2
1957     2
2004     2
1980     2
1997     2
1958     2
1983     2
1967     2
1986     2
1982     2
Name: count, dtype: int64

