import random
from typing import Annotated, Any, Dict, List

from fastapi import Body, FastAPI, Query, Response
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

MOCK_CREATOR_IDS = [
    ".bepdiiday._",
    "vienvibi_899",
    "minhnhatgk",
    "bepbepkute",
    "nongdan.vip2",
    "nguyen_huynh_tien",
    "thaovymuoimuoi",
    "swan_meii",
    "dorychang_03",
    "thuyn288",
    "banhmi.sociuu_",
    "maria_na_1016",
    "scarlet.199",
    "nhacomotconmeo20_06",
    "tocdep_moingay123",
    "m.chin2006",
    "khoedep62",
    "tpt.network",
    "zanggggxinhhh_",
    "phathuynhpham",
    "viet_anh_219",
    "mun.xinhh.depa",
    "20th2_007",
    "qquyquatqueoo",
    "trn.trang.77",
    "linhmy_060704",
    "hoaminzy_hoadambut",
    "vyvy.baby0312",
    "phuongthao..1984",
    "le_anh_nuoi",
    "henrytran001",
    "_qnhu_meow_",
    "necteam",
    "linh.remy",
    "_tthu2008_",
    "nmn.tec",
    "phuonghathaoshop",
    "return.9",
    "choi021102",
    "miacongchuahihi",
    "yame.vn",
    "janishalival",
    "dun_2000",
    "ducdiepstore",
    "duocmbappe",
    "n.chusa",
    "hothuongnichmoi",
    "huyentranguytin1",
    "quynhtrandaily",
    "dnkhaii",
    "vantruongvo84",
    "nam_dep_trai_official",
    "manhvu.8386",
    "aris29080",
    "viamiu",
    "kangooru_",
    "phimhayreview886",
    "tanvabowlki",
    "sgs.office",
    "ttn32",
    "d.dragon1712",
    "kiemkhachdatinh.qb",
    "trnkhnh2576",
    "tphng0909",
    "thegioithoitranghot2025",
    "bimatveshowbiz",
    "trunganhreview",
    "phuonginhanam95",
    "tranganna68",
    "misacutee_",
    "kenh7.life",
    "du_duong_tap_phoi_do",
    "tamlaoquy9999",
    "baoninh_01",
    "ntkt0168",
    "manhthichreview2k",
    "vochihieuu",
    "viabexinhyeu",
    "hapas.official",
    "maimo_10",
    "halanthachtung",
    "quochai2724",
    "ngth_hngoc",
    "takoharley",
    "vinhdztv369",
    "m_oanh00",
    "lamanh686868",
    "dau_hl",
    "hangsoyeu21",
    "thuthoeocute",
    "kenh247official",
    "vanhieuha58",
    "hoangphucst",
    "huynhlapofficial",
    "hahachaat",
    "vtvcab.sports",
    "nhatthien120797",
    "thangvy_live",
    "bbicuayou",
    "trang.shop94",
    "_hienhoinacs_",
    "huyn3535",
    "ngochuyen99998",
    "xuannhilamminhlammay",
    "lnna198",
    ".niii.2",
    "likyasb157",
    "cocaca102",
    "dandangam",
    "mysdynn",
    "knotshort",
    "pepi2k3",
    "_muonnghihee",
    "nutano4495",
    "ecochicvn",
    "du_duong_thu_hai",
    "chiphuongfishing",
    "ngoctocgia.vtt",
    "_trinhhavi_",
    "micha.vu",
    "trangnemo2024",
    "sen.xinh.shop",
    "mnoccutii",
    "huyk.trangsucchetac",
    "leminhtri2002",
    "khaaishop01",
    "lananhh_007",
    "ngocdau69",
    "thoitrangtrungnien_79",
    "minh_chien373",
    "nhoangthaibao",
    "ngandali2021",
    "linhnguyengianghia",
    "emthuythuyyy",
    "nhungloidanggia",
    "tomboyvietnam260615",
    "naniosaka",
    "igwnuong_63",
    "thanhphobuon82",
    "fbsangnguyen63",
    "anhvien0911",
    "tu30giay",
    "ngoc_hon15_09",
    "nimdayyy_",
    "xanhteo82",
    "zgangter",
    "leminh.1712",
    "vanviet.1994",
    "nhaanha_",
    "phatfreestyle",
    "lynguyn.2002",
    "lehuynhthuyngan91",
    "nguyenthanh512",
    "pth.official",
    "phhung_1210",
    "outfits_cua_lynh",
    "dacsanmientay3651",
    "anhthuu.2004",
    "duyen_158200",
    "nudienvien_1314",
    "ductuongquan2",
    "hoa3736",
    "cuclora",
    "tai335.com",
    "0yentuquan0",
    "user1y9dweevjr",
    "pingdiary",
    "luongtoanthang712",
    "quyenqueen03",
    "vinhbanhbo",
    "hatrungpr0vjp",
    "phongthuy_phamthuhien",
    "upperyou.vn",
    "mchibi02",
    "huyk.vienchibao1",
    "userngoctrang2603",
    "dieuminhchau11111",
    "vythang150",
    "chaumoe.dreamer",
    "thcongxautrai07",
    "thiencachot2",
    "trailaocaivn",
    "suavlauj48",
    "nhuquinhmeo",
    "pinn.black",
    "baolynee",
    "embegao2k7",
    "ny_nyvlog",
    "justbinhan",
    "thaygiaovungcaoymhg92",
    "thanhthanh19813",
    "vt_vanthanh2024",
    "tonly960",
    "anvy.boutique",
    "hungtt14",
    "_tumuoiot",
    "sassysis_br",
    "hueyyy998",
    "eb06thg9",
    "phungvanthang169",
    "trong94",
    "lamvuhoang2022",
    "chungnguyenfishing",
    "linhhai2002",
    "hangelsa",
    "anhthu20_8_4",
    "shenlongdang",
    "aimee2127",
    "quy99999999996",
    "anhtho2404",
    "thuybaby120604",
    "emmanguyen2410",
    "trainamgaibac",
    "casnhor68_",
    "_sandy4198",
    "lolystore99",
    "dat.tich.cuc",
    "ttic.04",
    "linh.khanh.65",
    "ecochicstory",
    "phamthuduytran",
    "trinhlunglinh96",
    "v.n.t.t",
    "jungyohan79",
    "sovintage_house",
    "buidinhthucvn",
    "haivansaovay",
    "letuankhangfc2003",
    "buntranstore2",
    "nguyn.th6162",
    "troxlacci",
    "bach.day9",
    "minhcungdivoinhau",
    "bpphuong98",
    "lhuongw_.1603",
    "matkinhvado",
    "shivast27",
    "nvkhanhhh",
    "bichson86",
    "xuongpolomin",
    "djcuibap.90",
    "giaynamnudep",
    "kimchi_store6868",
    "linh23052024",
    "nina.store.102",
    "h.khango_",
    "harry.nista",
    "nesty.store",
    "nguyentuong_147",
    "thocnhis",
    "namy6827",
    "thuonghoainn",
    "nidelanhaierb",
    "coswithnavii",
    "shopmytao",
    "nacute_.06",
    "akhoa.7",
    "quyenthaobui",
    "nanhi2089",
    "hienmuoi.vienchibao",
    "ksorhman12",
    "nga.143",
    "nilnh_7917",
    "thuykieu297",
    "giabao19na",
    "hienhoidieu",
    "tuan.vu321",
    "sunartvn",
    "ninhreview198",
    "co_giao_hien_69",
    "mei_chann_00",
    "thanhvuongreview",
    "soccerbeck.shop",
    "nam.perdz",
    "honganhdzaivocungluon",
    "dollie_nemayba",
    "tdat.review",
    "_coco1990",
    "binguyen10992",
    "thimeochuchoe",
    "triau942000",
    "simpson.vu",
    "kimphien170196",
    "gainhaycungme",
    "thoitrangtrungniena",
    "vlogminhhai",
    "1991.music.dj",
    "nhacsanhub2",
    "maonau99",
    "uyenchina0",
    "quynhtrangtui",
    "haalee27",
    "www.tiktok.com.hoangkk",
    "nhinsu",
    "thaobong996",
    "dinhlucsoccer",
    "ngocanhhhihihi",
    "phungphung8386",
    "faery_gem",
    "depthaifashion",
]

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3003",
        "https://mossdev.aduhay.dev",
        "https://affiliate.tiktok.com",
        #   "*"
    ],
    allow_origin_regex="chrome-extension://.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}


@app.get("/api/py/creator-ids")
async def get_creator_ids(
    limit: int = Query(default=10, ge=1, le=100)
) -> List[Dict[str, Any]]:
    return [{"id": id} for id in random.sample(MOCK_CREATOR_IDS, limit)]


@app.post("/api/py/creators")
async def create_creators(
    creators: Annotated[List[Dict[str, Any]], Body(...)],
) -> Response:
    [
        logger.info(f"Received creator {creator.id}: {creator.nickname}")
        for creator in creators
    ]

    return Response(status_code=200)


@app.post("/api/py/creators/errors")
async def create_creator_errors(
    errors: Annotated[List[Dict[str, Any]], Body(...)],
) -> Response:
    [
        logger.error(
            f"Error crawling creator {error.code} - {error.message}: {error.data}"
        )
        for error in errors
    ]

    return Response(status_code=200)
