import json
output_file = "33att_types.json"

ATT_LIST = "['ActiveIngredients','AgeRangeDescription','BatteryCellComposition','Brand','CaffeineContent','CapacityUnit','CoffeeRoastType','Color','DietType','DosageForm','EnergyUnit','FinishType','Flavor','FormulationType','HairType','Ingredients','ItemForm','ItemShape','LiquidContentsDescription','Material','MaterialFeature','MaterialTypeFree','PackageSizeName','Pattern','PatternType','ProductBenefit','Scent','SkinTone','SkinType','SpecialIngredients','TargetGender','TeaVariety','Variety']"
att_list = eval(ATT_LIST)

d = {"entities": {}, "relations": {}}
for att in att_list:
    d["entities"][att] = {"verbose": att, "short": att}

with open(output_file, 'w') as writer:
    json.dump(d, writer)