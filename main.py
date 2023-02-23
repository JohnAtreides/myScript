from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def root():
    return{"Hello": "World"}

@app.get("/kado/best10")
async def fetch_users():
    return best_10

best_10 = {
	"data": {
		"ten_best_buyers": [{
				"ID_CLIENT": "088326",
				"total_articles_bought": 398
			},
			{
				"ID_CLIENT": "222279",
				"total_articles_bought": 379
			},
			{
				"ID_CLIENT": "226918",
				"total_articles_bought": 834
			},
			{
				"ID_CLIENT": "266572",
				"total_articles_bought": 409
			},
			{
				"ID_CLIENT": "377988",
				"total_articles_bought": 426
			},
			{
				"ID_CLIENT": "453575",
				"total_articles_bought": 525
			},
			{
				"ID_CLIENT": "491953",
				"total_articles_bought": 608
			},
			{
				"ID_CLIENT": "571676",
				"total_articles_bought": 413
			},
			{
				"ID_CLIENT": "618679",
				"total_articles_bought": 502
			},
			{
				"ID_CLIENT": "754081",
				"total_articles_bought": 560
			},
		],
		"ten_best_sellers_by_famille": [{
				"ID_ARTICLE": "0000",
				"LIBELLE": "GD JDM4 PAMPLEMOUSSE FL 200 ML",
				"total_articles_sold": 888,
				"famille": "HYGIENE"
			},
			{
				"ID_ARTICLE": "0001",
				"LIBELLE": "CR JR PARF BIO.SPE AC.SENT.50ML",
				"total_articles_sold": 90,
				"famille": "MAQUILLAGE"
			},
			{
				"ID_ARTICLE": "0002",
				"LIBELLE": "EAU MICELLAIRE 3 THES FL200ML",
				"total_articles_sold": 109,
				"famille": "HYGIENE"
			},
			{
				"ID_ARTICLE": "0003",
				"LIBELLE": "GD JDM4 TIARE FL 200ML",
				"total_articles_sold": 286,
				"famille": "HYGIENE"
			},
			{
				"ID_ARTICLE": "0004",
				"LIBELLE": "EDT UN MATIN AU JARDIN 100 ML MUGUET ",
				"total_articles_sold": 456,
				"famille": "MAQUILLAGE"
			},
			{
				"ID_ARTICLE": "0005",
				"LIBELLE": "LAIT VELOUTE COCO PN2 400 ML ",
				"total_articles_sold": 965,
				"famille": "SOINS DU VISAGE"
			},
			{
				"ID_ARTICLE": "0006",
				"LIBELLE": "GD LILAS FP FL200ML",
				"total_articles_sold": 764,
				"famille": "SOINS DU VISAGE"
			},
			{
				"ID_ARTICLE": "0007",
				"LIBELLE": "LAIT LILAS FP FL200ML",
				"total_articles_sold": 145,
				"famille": "SOINS DU CORPS"
			},
			{
				"ID_ARTICLE": "0008",
				"LIBELLE": "EDT UN MATIN AU JARDIN 100ML LILAS",
				"total_articles_sold": 111,
				"famille": "MAQUILLAGE"
			},
			{
				"ID_ARTICLE": "0009",
				"LIBELLE": "RAL BRILLANC GEL/PRALIN CN3 2G",
				"total_articles_sold": 299,
				"famille": "MAQUILLAGE"
			},
		],
		"ten_best_sellers": [{
				"ID_ARTICLE": "0000",
				"LIBELLE": "GD JDM4 PAMPLEMOUSSE FL 200 ML",
				"total_articles_sold": 888
			},
			{
				"ID_ARTICLE": "0001",
				"LIBELLE": "CR JR PARF BIO.SPE AC.SENT.50ML",
				"total_articles_sold": 90
			},
			{
				"ID_ARTICLE": "0002",
				"LIBELLE": "EAU MICELLAIRE 3 THES FL200ML",
				"total_articles_sold": 109
			},
			{
				"ID_ARTICLE": "0003",
				"LIBELLE": "GD JDM4 TIARE FL 200ML",
				"total_articles_sold": 286
			},
			{
				"ID_ARTICLE": "0004",
				"LIBELLE": "EDT UN MATIN AU JARDIN 100 ML MUGUET ",
				"total_articles_sold": 456
			},
			{
				"ID_ARTICLE": "0005",
				"LIBELLE": "LAIT VELOUTE COCO PN2 400 ML ",
				"total_articles_sold": 965
			},
			{
				"ID_ARTICLE": "0006",
				"LIBELLE": "GD LILAS FP FL200ML",
				"total_articles_sold": 764
			},
			{
				"ID_ARTICLE": "0007",
				"LIBELLE": "LAIT LILAS FP FL200ML",
				"total_articles_sold": 145
			},
			{
				"ID_ARTICLE": "0008",
				"LIBELLE": "EDT UN MATIN AU JARDIN 100ML LILAS",
				"total_articles_sold": 111
			},
			{
				"ID_ARTICLE": "0009",
				"LIBELLE": "RAL BRILLANC GEL/PRALIN CN3 2G",
				"total_articles_sold": 299
			},
		],
		"user_List": [{
			"ID_CLIENT": "088326",
			"total_articles_bought": 888,
			"total_money_spent": 888,
			"most_bough_article": "GD JDM4 PAMPLEMOUSSE FL 200ML",
			"most_bough_article_famille": "HYGIENE"
		}, ],
		"perfect_present_for_user": [{
			"ID_CLIENT": "088326",
			"LIBELLE": "GD JDM4 PAMPLEMOUSSE FL 200ML",
			"famille": "HYGIENE",
			"price": 888
		}, ]
	}
}
