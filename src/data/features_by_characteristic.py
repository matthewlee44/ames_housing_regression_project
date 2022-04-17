id = ['Id', 'PID',]

land = ['MS SubClass', 'MS Zoning', 'Lot Frontage', 'Lot Area',
       'Street', 'Alley', 'Lot Shape', 'Land Contour', 'Utilities',
       'Lot Config', 'Land Slope', 'Neighborhood', 'Condition 1',
       'Condition 2',] 

building_general = ['Bldg Type', 'House Style', 'Overall Qual',
       'Overall Cond', 
]

building_age = ['Year Built', 'Year Remod/Add', 'Mo Sold', 'Yr Sold', 
]

building_exterior = [
       'Roof Style',
       'Roof Matl', 'Exterior 1st', 'Exterior 2nd', 'Mas Vnr Type',
       'Mas Vnr Area', 'Exter Qual', 'Exter Cond', 
]

basement = ['Foundation', 'Bsmt Qual',
       'Bsmt Cond', 'Bsmt Exposure', 'BsmtFin Type 1', 'BsmtFin SF 1',
       'BsmtFin Type 2', 'BsmtFin SF 2', 'Bsmt Unf SF', 'Total Bsmt SF',]

hvac = ['Heating', 'Heating QC', 'Central Air', 'Electrical', ]

interior = ['1st Flr SF',
       '2nd Flr SF', 'Low Qual Fin SF', 'Gr Liv Area', 'Bsmt Full Bath',
       'Bsmt Half Bath', 'Full Bath', 'Half Bath', 'Bedroom AbvGr',
       'Kitchen AbvGr', 'Kitchen Qual', 'TotRms AbvGrd', 'Functional',
]

garage = [
       'Garage Type', 'Garage Finish',
       'Garage Cars', 'Garage Area', 'Garage Qual', 'Garage Cond',
       'Paved Drive', 
]

misc = ['Wood Deck SF', 'Open Porch SF', 'Enclosed Porch',
       '3Ssn Porch', 'Screen Porch', 'Pool Area', 'Pool QC', 'Fence',
       'Misc Feature', 'Misc Val', 'Fireplaces', 'Fireplace Qu', ]

sale_type = ['Sale Type']

all_characteristics = {
       "id": id,
       "land": land,
       "building_general": building_general,
       "building_age": building_age,
       "building_exterior": building_exterior,
       "basement": basement,
       "hvac": hvac,
       "interior": interior,
       "garage": garage,
       "misc": misc,
       "sale_type": sale_type
}