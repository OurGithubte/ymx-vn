# -*- coding: utf-8 -*-
import os, datetime

OUT = os.environ.get("SITE_OUT", "/sessions/charming-elegant-archimedes/mnt/outputs")
YEAR = datetime.datetime.now().year

LANGS = ["vi", "en", "zh"]
LANG_LABEL = {"vi": "VI", "en": "EN", "zh": "中文"}
HTML_LANG = {"vi": "vi", "en": "en", "zh": "zh-CN"}
PAGES = ["index", "about", "products", "quality-hse", "contact"]

C = {}

# ---------------- VIETNAMESE ----------------
C["vi"] = dict(
    site_name="YMX VIỆT NAM", site_tag="ELECTRONIC TECHNOLOGY CO., LTD",
    nav=["Trang chủ","Giới thiệu","Sản phẩm & Ứng dụng","Thiết bị","Chất lượng & HSE","Liên hệ"],
    meta_title="YMX Việt Nam Electronic Technology | Cắt bế chính xác linh kiện điện tử",
    meta_desc="Công ty TNHH Electronic Technology YMX Việt Nam - chuyên sản xuất, gia công cắt bế chính xác linh kiện điện tử.",
    hero_eyebrow="Precision Die-Cutting Manufacturer",
    hero_pre="Chuyên gia cắt bế chính xác ", hero_em="linh kiện điện tử", hero_post="",
    hero_sub="Công ty TNHH Electronic Technology YMX Việt Nam là thành viên tại Việt Nam của tập đoàn YMX/Lingjiang Electronics (thành lập 2013), chuyên sản xuất và gia công cắt bế chính xác vật liệu điện tử công nghệ cao phục vụ điện thoại, máy tính, ô tô và thiết bị điện – điện tử toàn cầu.",
    cta1="Liên hệ hợp tác", cta2="Tìm hiểu công ty",
    stats=[("2013","Năm thành lập tập đoàn"),("6","Nhà máy toàn cầu (HK, Trung Quốc, Việt Nam)"),
           ("10 triệu","Sản phẩm/năm tại Việt Nam"),("1.484 m²","Diện tích nhà xưởng tại Đồng Nai")],
    home_intro_eyebrow="Về chúng tôi", home_intro_title="Về YMX Việt Nam",
    home_intro_text="Công ty TNHH Electronic Technology YMX Việt Nam (tên quốc tế: YMX Vietnam Electronic Technology Company Limited) là dự án đầu tư 100% vốn nước ngoài do Hongkong YMX Electronic Co., Limited làm chủ sở hữu, thuộc hệ thống tập đoàn Lingjiang Electronics được thành lập từ năm 2013, chuyên sâu trong lĩnh vực cắt bế chính xác (precision die-cutting) vật liệu điện tử phục vụ chuỗi cung ứng điện – điện tử toàn cầu.",
    home_intro_link="Xem thêm về công ty →",
    values_eyebrow="Giá trị cốt lõi", values_title="Kim chỉ nam hoạt động",
    values_sub="Bốn giá trị cốt lõi xuyên suốt trong quản trị và vận hành của tập đoàn, được kế thừa và áp dụng tại nhà máy Việt Nam.",
    values=[("诚","Chính trực (Integrity)","Trung thực là nền tảng của nhân cách, cạnh tranh công bằng, bình đẳng và hợp tác."),
            ("质","Chất lượng (Quality)","Lấy chất lượng làm trên hết, luôn mang lại sản phẩm và dịch vụ khiến khách hàng hài lòng."),
            ("服","Dịch vụ (Service)","Cam kết tạo dựng niềm tin khách hàng bằng dịch vụ chất lượng cao, hợp tác lâu dài."),
            ("发","Phát triển (Development)","Sử dụng hiệu quả mọi nguồn lực, cải tiến liên tục chất lượng, hướng tới vị thế hàng đầu ngành.")],
    cta_banner_title="Bạn cần đối tác cắt bế chính xác đáng tin cậy?", cta_banner_btn="Liên hệ ngay",
    about_eyebrow="Về chúng tôi", about_title="Giới thiệu Công ty",
    about_sub="Thông tin pháp lý và năng lực hoạt động của Công ty TNHH Electronic Technology YMX Việt Nam tại Khu công nghiệp Tam Phước, tỉnh Đồng Nai.",
    about_paras=[
        "Công ty TNHH Electronic Technology YMX Việt Nam (tên quốc tế: YMX Vietnam Electronic Technology Company Limited) là dự án đầu tư 100% vốn nước ngoài do Hongkong YMX Electronic Co., Limited làm chủ sở hữu, thuộc hệ thống tập đoàn Lingjiang Electronics được thành lập từ năm 2013, chuyên sâu trong lĩnh vực cắt bế chính xác (precision die-cutting) vật liệu điện tử.",
        "Với triết lý kinh doanh lấy chất lượng làm gốc, công ty tập trung phát triển và ứng dụng các vật liệu điện tử cao cấp, phục vụ chuỗi cung ứng cho điện thoại di động, ô tô, thiết bị gia dụng, thiết bị âm thanh, máy tính để bàn/laptop, máy tính bảng, máy in, máy photocopy, tivi và màn hình cảm ứng.",
        "Nhà máy được đầu tư dây chuyền sản xuất khép kín với các thiết bị hiện đại: máy cắt cuộn (slitting), máy cắt bế (die-cutting), máy ép lớp (laminating) và máy dập (stamping), đảm bảo năng lực sản xuất quy mô lớn với hệ thống kiểm tra – đo lường – thử nghiệm đồng bộ theo tiêu chuẩn của tập đoàn.",
        "Dự án nhà máy tại Việt Nam được Ban Quản lý các Khu công nghiệp, Khu kinh tế tỉnh Đồng Nai cấp Giấy chứng nhận đăng ký đầu tư, với mục tiêu sản xuất sản phẩm điện tử dân dụng (không xi mạ, không phủ màu bằng sơn/hóa chất, không làm sạch bằng hóa chất độc hại), quy mô 10.000.000 sản phẩm/năm, thời hạn hoạt động 50 năm, dự kiến chính thức đi vào vận hành từ tháng 4/2026.",
    ],
    legal_title="Thông tin pháp lý",
    legal_rows=[("Tên tiếng Việt","CÔNG TY TNHH ELECTRONIC TECHNOLOGY YMX VIỆT NAM"),
                ("Tên quốc tế","YMX VIETNAM ELECTRONIC TECHNOLOGY CO., LTD"),
                ("Mã số doanh nghiệp","3604072330"),
                ("Ngày đăng ký lần đầu","26/12/2025"),
                ("Vốn điều lệ","24.831.100.000 VNĐ (~950.000 USD)"),
                ("Chủ sở hữu","Hongkong YMX Electronic Co., Limited"),
                ("Người đại diện pháp luật","Ông Xu, Shaojun – Chủ tịch kiêm Giám đốc"),
                ("Ngành nghề chính (VSIC 2640)","Sản xuất sản phẩm điện tử dân dụng"),
                ("Địa điểm nhà xưởng","1.484 m² – Lô 33, KCN Tam Phước, Đồng Nai"),
                ("Thời hạn dự án","50 năm")],
    timeline_eyebrow="Hệ thống toàn cầu", timeline_title="Quá trình phát triển",
    timeline_sub="Từ nhà máy đầu tiên tại Hồng Kông năm 2013, tập đoàn đã mở rộng mạng lưới sản xuất cắt bế chính xác ra nhiều địa bàn, trong đó Việt Nam là mắt xích mới nhất phục vụ chuỗi cung ứng toàn cầu.",
    timeline=[("2013","YMX Electronics – Hồng Kông"),("2014","Lingjiang Electronics – Thâm Quyến"),
              ("2020","Lingjiang Electronics – Tô Châu"),("2021","Lingjiang Electronics – Uy Hải"),
              ("2022","Lingjiang Electronics – Giang Tây"),("2025–2026","YMX Electronics – Việt Nam (Đồng Nai)")],
    products_eyebrow="Sản phẩm & Ứng dụng", products_title="Sản phẩm & Ứng dụng",
    products_sub="Năng lực cạnh tranh cốt lõi và các lĩnh vực ứng dụng sản phẩm cắt bế chính xác của công ty.",
    strengths_eyebrow="Năng lực cạnh tranh", strengths_title="Bốn thế mạnh cốt lõi",
    strengths_sub="Nền tảng giúp công ty duy trì vị thế nhà cung cấp dịch vụ cắt bế chính xác chuyên nghiệp, ổn định và có tầm nhìn dài hạn.",
    strengths=[("Hệ thống đảm bảo chất lượng hoàn thiện","Kiểm soát chất lượng xuyên suốt từ nguyên liệu đầu vào đến thành phẩm xuất xưởng."),
               ("Hợp tác chiến lược nguyên vật liệu","Liên kết bền vững với các nhà sản xuất nguyên vật liệu điện tử uy tín."),
               ("Thiết bị & dụng cụ đo lường chuyên nghiệp","Dây chuyền cắt cuộn, cắt bế, ép lớp, dập khuôn hiện đại cùng thiết bị kiểm tra – hiệu chuẩn đồng bộ."),
               ("Dịch vụ trọn gói, vận hành nhất quán","Cung cấp giải pháp cắt bế một điểm dừng (one-stop service) cho khách hàng toàn cầu.")],
    apps_eyebrow="Ứng dụng sản phẩm", apps_title="Lĩnh vực & ứng dụng cắt bế chính xác",
    apps_sub="Sản phẩm cắt bế của công ty được ứng dụng rộng rãi trong nhiều ngành công nghiệp điện – điện tử và cơ khí.",
    apps=[("📠 Máy in / Photocopy",["Miếng đệm chống tĩnh điện, đệm kín – giảm chấn","Chi tiết hiệu chuẩn trong quá trình vận hành","Vật liệu dán ghép linh kiện, thấm hút mực dư","Sản phẩm dẫn điện và chống nhiễu (shielding)"],"printer"),
          ("📱 Điện thoại di động",["Băng keo 2 mặt dán màn hình, nắp lưng","Tấm tản nhiệt (graphite), màng lưới chống bụi","Màng bảo vệ, Poron, băng Kapton cố định mạch","Vật liệu dẫn điện, chống nhiễu điện từ"],"mobile"),
          ("💻 Máy tính xách tay",["Tấm nhựa PC/PP/PET chống trầy, trang trí","Bọt/vải dẫn điện, tấm dẫn nhiệt cho CPU","Tem nhãn cảnh báo, nhận diện sản phẩm","Băng keo 2 mặt, đồng/nhôm lá dẫn nhiệt"],"notebook"),
          ("💡 Module đèn nền (Backlight)",["Băng che sáng, tấm phản xạ, tấm khuếch tán","Màng tăng sáng, màng bảo vệ quang học","Mút đệm chống sốc, vật liệu chống nhiễu"],"backlight"),
          ("🚗 Ô tô / Pin",["Nỉ, PP/PC/PET nội thất, thảm sàn, trần xe","Băng keo 2 mặt dán logo, chống thấm","Bông hút âm, mút xốp giảm ồn cửa xe","Băng cách điện, chống cháy, dán quấn dây"],"automobile"),
          ("⚙️ Ứng dụng khác",["Tủ điện, tem nhãn hiệu suất năng lượng","Băng dán viền tấm pin năng lượng mặt trời","Vòng đệm silicone, băng chịu nhiệt độ cao","Gia công vật liệu đặc thù theo yêu cầu khách hàng"],"other")],
    product_detail_link="Xem chi tiết vật liệu →",
    back_to_products="← Quay lại Sản phẩm & Ứng dụng",
    materials_title="Vật liệu / linh kiện cắt bế tiêu biểu",
    equip_eyebrow="Thiết bị nhà máy", equip_title="Thiết bị sản xuất & Thiết bị kiểm tra",
    equip_sub="Hệ thống máy móc sản xuất và thiết bị đo lường, kiểm tra chất lượng đang được vận hành theo hướng dẫn công việc (PWI/QWI) tại nhà máy YMX Việt Nam.",
    equip_group_production="Thiết bị sản xuất",
    equip_group_testing="Thiết bị kiểm tra chất lượng",
    equip_detail_link="Xem chi tiết thiết bị →",
    back_to_equipment="← Quay lại Thiết bị",
    equip_specs_title="Thông số kỹ thuật tham khảo",
    equip_structure_title="Cấu tạo chính",
    equip_safety_title="⚠️ Lưu ý an toàn khi vận hành",
    equip_doc_label="Mã tài liệu hướng dẫn",
    qhse_eyebrow="Chất lượng & An toàn", qhse_title="Chất lượng & HSE",
    qhse_sub="Cam kết Chất lượng và An toàn - Sức khỏe - Môi trường (HSE) tại nhà máy Việt Nam.",
    quality_title="🛡️ Quản lý Chất lượng",
    quality_items=["Kiểm soát chất lượng đầu vào – quá trình – thành phẩm (IQC/IPQC/OQC)",
                   "Đồng bộ hệ thống quản lý chất lượng theo chuẩn tập đoàn tại các nhà máy Hồng Kông, Thâm Quyến, Tô Châu, Uy Hải, Giang Tây",
                   "Trang bị thiết bị đo lường, kiểm tra và hiệu chuẩn định kỳ",
                   "Kiểm soát hàng không phù hợp, xử lý CAPA/8D khi phát sinh lỗi",
                   "Truy xuất nguồn gốc theo mã lô sản xuất"],
    hse_title="⚠️ An toàn – Sức khỏe – Môi trường (HSE)",
    hse_items=["Tuân thủ pháp luật Việt Nam về lao động, an toàn, môi trường",
               "Nhận diện mối nguy, đánh giá và kiểm soát rủi ro tại hiện trường",
               "Trang bị bảo hộ lao động (PPE) theo từng vị trí công việc",
               "Kế hoạch phòng cháy chữa cháy (PCCC) và ứng phó sự cố khẩn cấp",
               "Quản lý hóa chất, chất thải theo quy định môi trường hiện hành"],
    policy_title="Định hướng chính sách chất lượng",
    policy_text="Sử dụng hợp lý mọi nguồn lực để đáp ứng kỳ vọng khách hàng, kiên trì cải tiến và hợp lý hóa quy trình liên tục, hướng đến mục tiêu tối thượng là sự hài lòng của khách hàng và phát triển bền vững – mang lại giá trị cho khách hàng, cổ đông, người lao động và cộng đồng.",
    contact_eyebrow="Liên hệ", contact_title="Liên hệ",
    contact_sub="Công ty TNHH Electronic Technology YMX Việt Nam sẵn sàng trao đổi hợp tác cùng khách hàng và đối tác.",
    contact_items=[("📍","Địa chỉ nhà máy","Nhà xưởng 3A, Lô 33, Khu công nghiệp Tam Phước, Phường Tam Phước, Tỉnh Đồng Nai, Việt Nam"),
                   ("🏢","Mã số doanh nghiệp","3604072330"),
                   ("👤","Người đại diện theo pháp luật","Ông Xu, Shaojun – Chủ tịch kiêm Giám đốc"),
                   ("✉️","Email","steven@ljdzsz.com"),
                   ("☎️","Điện thoại","0086-18680875176")],
    footer_legal="Công ty TNHH Electronic Technology YMX Việt Nam – MSDN 3604072330, đăng ký lần đầu ngày 26/12/2025 tại Sở Tài chính tỉnh Đồng Nai. Dự án đầu tư được cấp Giấy chứng nhận đăng ký đầu tư bởi Ban Quản lý các Khu công nghiệp, Khu kinh tế tỉnh Đồng Nai.",
    copyright=f"© {YEAR} YMX Vietnam Electronic Technology Company Limited. All rights reserved.",
)
print("VI content length ok")

# ---------------- ENGLISH ----------------
C["en"] = dict(
    site_name="YMX VIETNAM", site_tag="ELECTRONIC TECHNOLOGY CO., LTD",
    nav=["Home","About Us","Products & Applications","Equipment","Quality & HSE","Contact"],
    meta_title="YMX Vietnam Electronic Technology | Precision Die-Cutting Manufacturer",
    meta_desc="YMX Vietnam Electronic Technology Company Limited - precision die-cutting manufacturing for electronic components.",
    hero_eyebrow="Precision Die-Cutting Manufacturer",
    hero_pre="Precision die-cutting experts for ", hero_em="electronic components", hero_post="",
    hero_sub="YMX Vietnam Electronic Technology Company Limited is the Vietnam member of the YMX/Lingjiang Electronics Group (founded 2013), specializing in the manufacture and precision die-cutting of advanced electronic materials for mobile phones, computers, automobiles and electrical/electronic equipment worldwide.",
    cta1="Get in Touch", cta2="Learn About Us",
    stats=[("2013","Year the Group was founded"),("6","Global factories (HK, China, Vietnam)"),
           ("10 million","Products/year in Vietnam"),("1,484 m²","Factory area in Dong Nai")],
    home_intro_eyebrow="About Us", home_intro_title="About YMX Vietnam",
    home_intro_text="YMX Vietnam Electronic Technology Company Limited is a 100% foreign-invested project owned by Hongkong YMX Electronic Co., Limited, part of the Lingjiang Electronics Group founded in 2013, specializing in precision die-cutting of electronic materials for the global electrical/electronics supply chain.",
    home_intro_link="Learn more about the company →",
    values_eyebrow="Core Values", values_title="Our Guiding Principles",
    values_sub="Four core values that guide the Group's management and operations, inherited and applied at the Vietnam factory.",
    values=[("诚","Integrity","We believe honesty is the foundation of character, fair competition, equality and cooperation."),
            ("质","Quality","We put quality first, always delivering products and services that satisfy our customers."),
            ("服","Service","We are committed to earning customer trust through high-quality service and long-term partnership."),
            ("发","Development","We make effective use of all resources, continuously improve quality, and strive to lead the industry.")],
    cta_banner_title="Looking for a reliable precision die-cutting partner?", cta_banner_btn="Contact Us Now",
    about_eyebrow="About Us", about_title="About the Company",
    about_sub="Legal information and operational capabilities of YMX Vietnam Electronic Technology Company Limited at Tam Phuoc Industrial Park, Dong Nai Province.",
    about_paras=[
        "YMX Vietnam Electronic Technology Company Limited (Vietnamese name: CÔNG TY TNHH ELECTRONIC TECHNOLOGY YMX VIỆT NAM) is a 100% foreign-invested project owned by Hongkong YMX Electronic Co., Limited, part of the Lingjiang Electronics Group founded in 2013, specializing in precision die-cutting of electronic materials.",
        "Guided by a quality-first business philosophy, the company focuses on developing and applying advanced electronic materials, serving the supply chains of mobile phones, automobiles, home appliances, audio devices, desktop/laptop computers, tablets, printers, copiers, televisions and touch screens.",
        "The factory is equipped with a complete, modern production line including slitting machines, die-cutting machines, laminating systems and stamping equipment, ensuring large-scale production capacity backed by an inspection, measurement and testing system aligned with Group standards.",
        "The Vietnam factory project has been granted an Investment Registration Certificate by the Management Board of Industrial Zones and Economic Zones of Dong Nai Province, targeting the manufacture of consumer electronic products (excluding electroplating, paint/chemical coating and toxic chemical cleaning), with a capacity of 10,000,000 products/year, a 50-year operating term, and is expected to officially commence operations from April 2026.",
    ],
    legal_title="Legal Information",
    legal_rows=[("Vietnamese Name","CÔNG TY TNHH ELECTRONIC TECHNOLOGY YMX VIỆT NAM"),
                ("International Name","YMX VIETNAM ELECTRONIC TECHNOLOGY CO., LTD"),
                ("Enterprise Code","3604072330"),
                ("First Registration Date","26 December 2025"),
                ("Charter Capital","VND 24,831,100,000 (~USD 950,000)"),
                ("Owner","Hongkong YMX Electronic Co., Limited"),
                ("Legal Representative","Mr. Xu, Shaojun – Chairman cum Director"),
                ("Main Business Line (VSIC 2640)","Manufacture of consumer electronic products"),
                ("Factory Location","1,484 m² – Lot 33, Tam Phuoc Industrial Park, Dong Nai"),
                ("Project Term","50 years")],
    timeline_eyebrow="Global Network", timeline_title="Development Journey",
    timeline_sub="Since its first factory in Hong Kong in 2013, the Group has expanded its precision die-cutting production network, with Vietnam as the newest link serving the global supply chain.",
    timeline=[("2013","YMX Electronics – Hong Kong"),("2014","Lingjiang Electronics – Shenzhen"),
              ("2020","Lingjiang Electronics – Suzhou"),("2021","Lingjiang Electronics – Weihai"),
              ("2022","Lingjiang Electronics – Jiangxi"),("2025–2026","YMX Electronics – Vietnam (Dong Nai)")],
    products_eyebrow="Products & Applications", products_title="Products & Applications",
    products_sub="Core competitive strengths and the main application fields of the company's precision die-cut products.",
    strengths_eyebrow="Competitive Strengths", strengths_title="Four Core Strengths",
    strengths_sub="The foundation that helps the company maintain its position as a professional, stable, forward-looking precision die-cutting service provider.",
    strengths=[("Complete Quality Assurance System","Consistent quality control from incoming raw materials to finished goods shipment."),
               ("Strategic Raw Material Partnerships","Stable strategic cooperation with reputable electronic material manufacturers."),
               ("Professional Equipment & Testing Instruments","Modern slitting, die-cutting, laminating and stamping lines with synchronized inspection and calibration equipment."),
               ("One-Stop Service, Consistent Operation","Providing one-stop die-cutting solutions for customers worldwide.")],
    apps_eyebrow="Product Applications", apps_title="Precision Die-Cutting Application Fields",
    apps_sub="The company's die-cut products are widely used across many electrical, electronic and mechanical industries.",
    apps=[("📠 Printer / Copier",["Anti-static pads, sealing & shock-absorbing cushions","Calibration components used during operation","Component bonding materials, ink-absorbing materials","Conductive and EMI shielding materials"],"printer"),
          ("📱 Mobile Phone",["Double-sided tape for screen and back cover bonding","Graphite heat sinks, dust-proof mesh","Protective film, Poron foam, Kapton tape for circuit fixing","Conductive and EMI shielding materials"],"mobile"),
          ("💻 Notebook Computer",["PC/PP/PET anti-scratch, decorative panels","Conductive foam/cloth, thermal pads for CPU","Warning labels and product identification","Double-sided tape, thermal copper/aluminum foil"],"notebook"),
          ("💡 Backlight Module",["Light-blocking tape, reflective sheet, diffusion sheet","Brightness enhancement film, optical protective film","Shock-absorbing foam, shielding materials"],"backlight"),
          ("🚗 Automobile / Battery",["Felt, PP/PC/PET interior trim, carpet, headliner","Double-sided tape for logo bonding and waterproofing","Sound-absorbing cotton, noise-reduction foam for doors","Insulating, fire-resistant tape and wire-wrapping materials"],"automobile"),
          ("⚙️ Other Applications",["Electrical cabinets, energy efficiency labels","Edge-sealing tape for photovoltaic panels","Silicone sealing rings, high-temperature tape","Custom processing of special materials per customer request"],"other")],
    product_detail_link="View material details →",
    back_to_products="← Back to Products & Applications",
    materials_title="Featured Die-Cut Materials & Components",
    equip_eyebrow="Factory Equipment", equip_title="Production & Testing Equipment",
    equip_sub="Production machinery and quality inspection/measurement equipment operated according to work instructions (PWI/QWI) at the YMX Vietnam factory.",
    equip_group_production="Production Equipment",
    equip_group_testing="Quality Testing Equipment",
    equip_detail_link="View equipment details →",
    back_to_equipment="← Back to Equipment",
    equip_specs_title="Reference Technical Specifications",
    equip_structure_title="Main Structure",
    equip_safety_title="⚠️ Operating Safety Notes",
    equip_doc_label="Work Instruction Code",
    qhse_eyebrow="Quality & Safety", qhse_title="Quality & HSE",
    qhse_sub="Our commitment to Quality and Health-Safety-Environment (HSE) at the Vietnam factory.",
    quality_title="🛡️ Quality Management",
    quality_items=["Incoming, in-process and outgoing quality control (IQC/IPQC/OQC)",
                   "Quality management system aligned with Group standards across Hong Kong, Shenzhen, Suzhou, Weihai and Jiangxi factories",
                   "Measurement, inspection and calibration equipment maintained on schedule",
                   "Nonconforming product control, CAPA/8D corrective actions when issues arise",
                   "Traceability by production batch code"],
    hse_title="⚠️ Health, Safety & Environment (HSE)",
    hse_items=["Compliance with Vietnamese labor, safety and environmental regulations",
               "On-site hazard identification, risk assessment and control",
               "Personal protective equipment (PPE) provided per job position",
               "Fire prevention and fighting (PCCC) and emergency response plans",
               "Chemical and waste management in accordance with current environmental regulations"],
    policy_title="Quality Policy Direction",
    policy_text="Make rational use of all resources to meet customer expectations, persistently improve and rationalize processes, with the ultimate goal of customer satisfaction and sustainable development — creating value for customers, shareholders, employees and society.",
    contact_eyebrow="Contact", contact_title="Contact Us",
    contact_sub="YMX Vietnam Electronic Technology Company Limited welcomes cooperation with customers and partners.",
    contact_items=[("📍","Factory Address","Workshop 3A, Lot 33, Tam Phuoc Industrial Park, Tam Phuoc Ward, Dong Nai Province, Vietnam"),
                   ("🏢","Enterprise Code","3604072330"),
                   ("👤","Legal Representative","Mr. Xu, Shaojun – Chairman cum Director"),
                   ("✉️","Email","steven@ljdzsz.com"),
                   ("☎️","Phone","0086-18680875176")],
    footer_legal="YMX Vietnam Electronic Technology Company Limited – Enterprise Code 3604072330, first registered on 26 December 2025 at the Dong Nai Provincial Department of Finance. The investment project was granted an Investment Registration Certificate by the Management Board of Industrial Zones and Economic Zones of Dong Nai Province.",
    copyright=f"© {YEAR} YMX Vietnam Electronic Technology Company Limited. All rights reserved.",
)
print("EN content length ok")

# ---------------- CHINESE (Simplified) ----------------
C["zh"] = dict(
    site_name="越南YMX", site_tag="ELECTRONIC TECHNOLOGY CO., LTD",
    nav=["首页","公司简介","产品与应用","设备","质量与HSE","联系我们"],
    meta_title="越南YMX电子科技有限公司 | 精密模切制造专家",
    meta_desc="越南YMX电子科技有限公司 - 专注电子元器件精密模切生产与加工。",
    hero_eyebrow="精密模切制造专家",
    hero_pre="专业电子元器件", hero_em="精密模切", hero_post="制造专家",
    hero_sub="越南YMX电子科技有限公司是YMX/领将电子集团（成立于2013年）在越南的成员企业，专注于高端电子材料的精密模切生产与加工，服务于全球手机、电脑、汽车及电子电器供应链。",
    cta1="联系合作", cta2="了解公司",
    stats=[("2013","集团成立年份"),("6","全球工厂（香港、中国大陆、越南）"),
           ("1000万","越南工厂年产能（件/年）"),("1,484平方米","同奈省厂房面积")],
    home_intro_eyebrow="关于我们", home_intro_title="关于越南YMX",
    home_intro_text="越南YMX电子科技有限公司是由香港YMX电子有限公司100%控股投资的项目，隶属于成立于2013年的领将电子集团体系，专注于电子材料精密模切（Die-Cutting）领域，服务全球电子电器供应链。",
    home_intro_link="了解更多公司信息 →",
    values_eyebrow="核心价值观", values_title="经营指导方针",
    values_sub="集团经营管理中始终坚持的四大核心价值观，并在越南工厂得到传承与落实。",
    values=[("诚","诚信 (Integrity)","诚信是人格、公平竞争、平等合作的基础。"),
            ("质","质量 (Quality)","坚持质量第一，始终为客户提供满意的产品与服务。"),
            ("服","服务 (Service)","以优质服务赢得客户信任，追求长期合作。"),
            ("发","发展 (Development)","合理运用一切资源，持续改进质量，致力成为行业一流企业。")],
    cta_banner_title="需要值得信赖的精密模切合作伙伴？", cta_banner_btn="立即联系",
    about_eyebrow="关于我们", about_title="公司简介",
    about_sub="越南YMX电子科技有限公司位于同奈省仁泽工业区的法律信息及运营能力介绍。",
    about_paras=[
        "越南YMX电子科技有限公司（英文名：YMX Vietnam Electronic Technology Company Limited）是由香港YMX电子有限公司（Hongkong YMX Electronic Co., Limited）100%控股投资的项目，隶属于成立于2013年的领将电子集团体系，专注于电子材料的精密模切（Die-Cutting）领域。",
        "秉承以质量为本的经营理念，公司致力于高端电子材料的开发与应用，产品广泛服务于手机、汽车、家电、音响设备、台式机/笔记本电脑、平板电脑、打印机、复印机、电视及触摸屏等产业供应链。",
        "工厂投资建设了完整的生产线，配备分条机、模切机、贴合机及冲压机等先进设备，确保大规模生产能力，并配套集团标准的检测、计量与测试体系。",
        "越南工厂项目已获同奈省工业区与经济区管理委员会颁发的《投资登记证》，生产目标为民用电子产品（不含电镀、油漆/化学品涂色及有毒化学品清洗工序），规模为年产1000万件，项目经营期限50年，预计于2026年4月正式投产。",
    ],
    legal_title="法律信息",
    legal_rows=[("越南文名称","CÔNG TY TNHH ELECTRONIC TECHNOLOGY YMX VIỆT NAM"),
                ("英文名称","YMX VIETNAM ELECTRONIC TECHNOLOGY CO., LTD"),
                ("企业代码","3604072330"),
                ("首次注册日期","2025年12月26日"),
                ("注册资本","24,831,100,000越南盾（约95万美元）"),
                ("股东（所有者）","香港YMX电子有限公司"),
                ("法定代表人","徐少军（Xu, Shaojun）先生 – 董事长兼总经理"),
                ("主要行业（VSIC 2640）","民用电子产品制造"),
                ("厂房位置","同奈省仁泽工业区33号地块，面积1,484平方米"),
                ("项目期限","50年")],
    timeline_eyebrow="全球布局", timeline_title="发展历程",
    timeline_sub="自2013年香港首家工厂成立以来，集团精密模切生产网络不断扩张，越南是服务全球供应链的最新一环。",
    timeline=[("2013","YMX电子 – 香港"),("2014","领将电子 – 深圳"),
              ("2020","领将电子 – 苏州"),("2021","领将电子 – 威海"),
              ("2022","领将电子 – 江西"),("2025–2026","YMX电子 – 越南（同奈）")],
    products_eyebrow="产品与应用", products_title="产品与应用",
    products_sub="公司核心竞争优势及精密模切产品的主要应用领域。",
    strengths_eyebrow="核心竞争力", strengths_title="四大核心优势",
    strengths_sub="支撑公司保持专业、稳定且具有长远发展眼光的精密模切服务提供商地位的基础。",
    strengths=[("完善的质量保证体系","从原材料进厂到成品出货的全流程质量管控。"),
               ("原材料战略合作","与知名电子材料供应商建立稳定的战略合作关系。"),
               ("专业设备与检测仪器","分条、模切、贴合、冲压等先进产线，配套同步的检测校准设备。"),
               ("一站式服务，运营稳定一致","为全球客户提供一站式模切解决方案。")],
    apps_eyebrow="产品应用", apps_title="精密模切应用领域",
    apps_sub="公司模切产品广泛应用于多个电子、电气及机械制造领域。",
    apps=[("📠 打印机/复印机",["防静电垫片、密封缓冲垫","运行过程中的校准元件","元件粘贴材料、吸墨材料","导电及电磁屏蔽材料"],"printer"),
          ("📱 移动电话",["屏幕、后盖双面胶","石墨散热片、防尘网","保护膜、Poron泡棉、固定电路用Kapton胶带","导电及电磁屏蔽材料"],"mobile"),
          ("💻 笔记本电脑",["PC/PP/PET防刮、装饰板材","导电泡棉/导电布、CPU导热片","警示标签、产品标识","双面胶、导热铜箔/铝箔"],"notebook"),
          ("💡 背光模组",["遮光胶带、反射片、扩散片","增亮膜、光学保护膜","缓冲泡棉、屏蔽材料"],"backlight"),
          ("🚗 汽车/电池",["内饰毛毡、PP/PC/PET地毯顶棚","双面胶（车标粘贴、防水）","吸音棉、隔音泡棉（车门）","绝缘、阻燃胶带及包线材料"],"automobile"),
          ("⚙️ 其他应用",["配电柜、能效标签","光伏板边框封装胶带","硅胶密封圈、耐高温胶带","按客户需求定制特殊材料加工"],"other")],
    product_detail_link="查看材料详情 →",
    back_to_products="← 返回产品与应用",
    materials_title="典型模切材料与部件",
    equip_eyebrow="工厂设备", equip_title="生产设备与检测设备",
    equip_sub="越南YMX工厂内按作业指导书（PWI/QWI）运行的生产机台及品质检测/计量设备。",
    equip_group_production="生产设备",
    equip_group_testing="品质检测设备",
    equip_detail_link="查看设备详情 →",
    back_to_equipment="← 返回设备",
    equip_specs_title="参考技术参数",
    equip_structure_title="主要结构",
    equip_safety_title="⚠️ 操作安全注意事项",
    equip_doc_label="作业指导书编号",
    qhse_eyebrow="质量与安全", qhse_title="质量与HSE",
    qhse_sub="越南工厂在质量管理与健康-安全-环境（HSE）方面的承诺。",
    quality_title="🛡️ 质量管理",
    quality_items=["来料/制程/成品检验管控（IQC/IPQC/OQC）",
                   "与香港、深圳、苏州、威海、江西各厂同步的集团质量管理体系",
                   "配备计量检测设备，并定期校准",
                   "不合格品管控，异常发生时执行CAPA/8D纠正预防措施",
                   "按生产批号实现质量追溯"],
    hse_title="⚠️ 安全-健康-环境（HSE）",
    hse_items=["遵守越南劳动、安全及环境相关法律法规",
               "现场危害识别、风险评估与管控",
               "按岗位配备劳动防护用品（PPE）",
               "制定消防（PCCC）及应急预案",
               "按现行环保法规管理化学品与废弃物"],
    policy_title="质量方针",
    policy_text="合理运用各项资源以满足客户期望，坚持流程合理化与持续改进，最终目标是让客户满意，并实现可持续发展——为客户、股东、员工及社会创造价值。",
    contact_eyebrow="联系我们", contact_title="联系我们",
    contact_sub="越南YMX电子科技有限公司欢迎与客户及合作伙伴洽谈合作。",
    contact_items=[("📍","工厂地址","越南同奈省仁泽坊仁泽工业区33号地块3A厂房"),
                   ("🏢","企业代码","3604072330"),
                   ("👤","法定代表人","徐少军（Xu, Shaojun）先生 – 董事长兼总经理"),
                   ("✉️","邮箱","steven@ljdzsz.com"),
                   ("☎️","电话","0086-18680875176")],
    footer_legal="越南YMX电子科技有限公司 – 企业代码3604072330，于2025年12月26日在同奈省财政厅首次注册。投资项目已获同奈省工业区与经济区管理委员会颁发投资登记证书。",
    copyright=f"© {YEAR} YMX Vietnam Electronic Technology Company Limited. All rights reserved.",
)
print("ZH content length ok")

# ---------------- PRODUCT DETAIL PAGES (materials + images) ----------------
# materials: (name, image_filename_in_assets/products/<slug>/, description)
PRODUCT_DETAIL = {}

PRODUCT_DETAIL["vi"] = {
  "printer": dict(
    title="Máy in / Photocopy", hero="hero.jpg",
    subtitle="Các vật liệu cắt bế chính xác được lắp bên trong máy in, máy photocopy để hỗ trợ vận hành ổn định và bền bỉ.",
    intro=["Máy in và máy photocopy sử dụng nhiều linh kiện cắt bế chính xác cho các cụm cơ khí và điện tử bên trong: từ dải hiệu chuẩn cảm biến, đến vật liệu hút mực dư, đệm giảm chấn và chổi khử tĩnh điện. Đây là những chi tiết nhỏ nhưng quyết định độ chính xác và tuổi thọ vận hành của thiết bị."],
    materials=[
      ("Dải hiệu chuẩn","calibration-strip.png","Dùng để hiệu chuẩn vị trí đầu in/cảm biến trong quá trình vận hành, đảm bảo độ chính xác khi in ấn."),
      ("Bông thấm mực","ink-absorbing-cotton.jpg","Vật liệu xốp cắt bế theo hình dạng khay mực, hút và giữ lượng mực dư thừa từ đầu phun."),
      ("Băng dán kỹ thuật","tape.png","Băng dán chuyên dụng cố định linh kiện bên trong máy in trong quá trình lắp ráp."),
      ("Bìa ép định hình","pressed-cardboard.png","Tấm bìa ép cắt bế dùng làm khung đỡ, cách điện hoặc định vị linh kiện."),
      ("Mút xốp","foam.png","Đệm giảm chấn, chống trầy xước cho các bộ phận chuyển động trong máy in."),
      ("Chổi khử tĩnh điện","electrostatic-brush.png","Dạng lược cắt bế dùng để trung hòa tĩnh điện sinh ra khi giấy di chuyển qua máy in."),
    ],
  ),
  "mobile": dict(
    title="Điện thoại di động", hero="hero.png",
    subtitle="Bộ vật liệu cắt bế chính xác cấu thành nên một chiếc điện thoại thông minh, từ khung sườn đến các lớp tản nhiệt, bảo vệ.",
    intro=["Điện thoại di động là sản phẩm điện tử có mật độ linh kiện cao nhất trong các ứng dụng cắt bế của công ty. Mỗi chiếc điện thoại cần hàng chục chi tiết cắt bế chính xác đến từng milimet để dán, cố định, tản nhiệt, chống bụi và bảo vệ các linh kiện bên trong."],
    materials=[
      ("Băng keo 2 mặt","double-sided-tape.png","Dán cố định màn hình và nắp lưng điện thoại."),
      ("Tấm than chì (Graphite)","graphite.png","Tản nhiệt cho các linh kiện sinh nhiệt như chip xử lý, pin."),
      ("Lưới chống bụi","dust-proof-net.png","Lưới lọc lắp tại khu vực loa/microphone để ngăn bụi xâm nhập."),
      ("Màng bảo vệ","protective-film.png","Bảo vệ bề mặt màn hình/vỏ máy trong quá trình lắp ráp và vận chuyển."),
      ("Mút Poron","poron.png","Đệm giảm chấn, chống sốc và làm kín các khe hở bên trong máy."),
      ("Băng Kapton","kapton.png","Băng chịu nhiệt cao dùng cố định mạch/cáp dẹt (FPC) bên trong máy."),
    ],
  ),
  "notebook": dict(
    title="Máy tính xách tay", hero="hero.png",
    subtitle="Vật liệu cắt bế phục vụ lắp ráp, tản nhiệt và nhận diện sản phẩm cho laptop.",
    intro=["Bên trong một chiếc laptop là hệ thống linh kiện phức tạp cần được cố định, cách điện, dẫn nhiệt và bảo vệ đúng vị trí. Các sản phẩm cắt bế chính xác giúp đảm bảo từng lớp linh kiện được lắp ráp gọn gàng, tản nhiệt hiệu quả và đạt chuẩn nhận diện thương hiệu."],
    materials=[
      ("Tấm nhựa PC/PP/PET","pc-pp-pet.png","Tấm nhựa kỹ thuật cắt bế dùng trang trí, chống trầy bề mặt máy."),
      ("Bọt/vải dẫn điện","conductive-foam-cloth-tape.png","Vật liệu dẫn điện, chống nhiễu điện từ (EMI) cho bo mạch."),
      ("Tem nhãn","label.png","Tem nhãn nhận diện cấu hình (chip, hệ điều hành, chứng nhận bản quyền...)."),
      ("Lá đồng / nhôm","copper-aluminum-foil.png","Lá kim loại dẫn nhiệt, dẫn điện và chống nhiễu cho các khu vực mạch."),
      ("Tấm dẫn nhiệt","thermal-conductive-sheet.png","Tấm dẫn nhiệt gắn giữa linh kiện và bộ tản nhiệt."),
      ("Băng keo 2 mặt","double-sided-tape.png","Cố định các lớp linh kiện bên trong laptop."),
    ],
  ),
  "backlight": dict(
    title="Module đèn nền (Backlight)", hero="hero.png",
    subtitle="Các lớp vật liệu quang học cắt bế chính xác tạo nên module đèn nền cho màn hình LCD.",
    intro=["Module đèn nền là một cấu trúc nhiều lớp quang học xếp chồng, mỗi lớp đảm nhiệm một chức năng riêng: dẫn sáng, khuếch tán, tăng sáng, phản xạ và che sáng. Độ chính xác kích thước của từng lớp cắt bế ảnh hưởng trực tiếp đến chất lượng hiển thị của màn hình."],
    materials=[
      ("Băng che sáng","light-blocking-tape.png","Ngăn ánh sáng rò rỉ ra ngoài module đèn nền."),
      ("Tấm phản xạ","reflective-sheet.png","Phản xạ ánh sáng trở lại để tăng hiệu suất chiếu sáng."),
      ("Tấm khuếch tán","diffusion-sheet.png","Khuếch tán ánh sáng đồng đều trên bề mặt màn hình."),
      ("Màng tăng sáng (BEF)","brightness-enhancement-film.png","Tăng cường độ sáng và độ đồng đều ánh sáng."),
      ("Màng bảo vệ","protective-film.png","Bảo vệ bề mặt các lớp quang học trong quá trình lắp ráp."),
      ("Mút đệm","foam.png","Đệm chống sốc, cố định các lớp trong module đèn nền."),
    ],
  ),
  "automobile": dict(
    title="Ô tô / Pin", hero="hero.png",
    subtitle="Vật liệu cắt bế cho nội thất, cách âm và pin xe điện.",
    intro=["Trong ngành ô tô và pin xe điện, vật liệu cắt bế chính xác được dùng rộng rãi cho nội thất, cách âm, chống thấm và cố định các cụm pin. Yêu cầu về độ bền, khả năng chịu nhiệt và chống rung cao hơn nhiều so với các ứng dụng điện tử tiêu dùng thông thường."],
    materials=[
      ("Nỉ (Felt)","felt.png","Lót nỉ giảm ồn, chống trầy cho nội thất và khoang máy."),
      ("Băng keo 2 mặt","double-sided-tape.png","Dán cố định logo xe và các chi tiết chống thấm."),
      ("Tấm nhựa PP/PC/PET","pp-pc-pet.png","Dùng cho thảm sàn, ốp trần, hộp đựng nội thất."),
      ("Bông hút âm","sound-absorbing-cotton.png","Gắn trong cửa xe, giảm tiếng ồn."),
      ("Mút xốp","sponge.png","Đệm chống rung và bụi cho các mối ghép."),
      ("Giấy đệm (Barley paper)","barley-paper.png","Giấy đệm/joăng dùng làm kín và cách nhiệt tại các mối ghép."),
    ],
  ),
  "other": dict(
    title="Ứng dụng khác", hero=None,
    subtitle="Các vật liệu cắt bế đặc thù phục vụ tủ điện, thiết bị gia dụng và năng lượng mặt trời.",
    intro=["Ngoài các ứng dụng chính, công ty còn nhận gia công cắt bế nhiều loại vật liệu đặc thù theo yêu cầu khách hàng cho tủ điện công nghiệp, thiết bị gia dụng, tấm pin năng lượng mặt trời và nhiều lĩnh vực khác."],
    materials=[
      ("Tủ điện", None, "Tem nhãn, vật liệu cách điện dùng trong tủ điện công nghiệp."),
      ("Băng keo silicone","silicone-tape.png","Băng chịu nhiệt, không để lại keo dư, dùng cố định bộ phận chuyển động khi vận chuyển (ví dụ tủ lạnh)."),
      ("Băng chịu nhiệt độ cao","high-temperature-tape.png","Độ bám dính tốt, chịu nhiệt và chống dung môi hóa chất, dùng trong thiết bị điện tử."),
      ("Tem nhãn năng lượng","energy-efficiency-label.png","Tem nhãn hiệu suất năng lượng dán trên thiết bị điện gia dụng."),
      ("Băng bọc viền tấm pin mặt trời","pv-edge-tape.png","Băng PET bọc viền tấm pin năng lượng mặt trời."),
      ("Vòng đệm (Sealing ring)","sealing-ring.png","Vòng đệm cắt từ silicone/mút, dùng làm kín, chống rung."),
      ("Băng đặc thù","special-tape.png","Gia công cắt bế các loại băng đặc thù theo yêu cầu khách hàng (băng pin điện thoại, băng chống thấm, khẩu trang không dệt...)."),
    ],
  ),
}

PRODUCT_DETAIL["en"] = {
  "printer": dict(
    title="Printer / Copier", hero="hero.jpg",
    subtitle="Precision die-cut materials fitted inside printers and copiers to support stable, long-lasting operation.",
    intro=["Printers and copiers rely on many precision die-cut components for their internal mechanical and electronic assemblies: calibration strips for sensors, ink-absorbing materials, shock-absorbing cushions and anti-static brushes. These are small details that determine the accuracy and operating lifespan of the equipment."],
    materials=[
      ("Calibration Strip","calibration-strip.png","Used to calibrate the print head/sensor position during operation, ensuring printing accuracy."),
      ("Ink-Absorbing Cotton","ink-absorbing-cotton.jpg","Die-cut foam shaped to the ink tray, absorbing and holding excess ink from the print head."),
      ("Technical Tape","tape.png","Specialized tape used to secure internal components during assembly."),
      ("Pressed Cardboard","pressed-cardboard.png","Die-cut pressed board used as a support frame, insulator, or component positioner."),
      ("Foam","foam.png","Shock-absorbing, scratch-protection cushion for moving parts inside the printer."),
      ("Electrostatic Brush","electrostatic-brush.png","Comb-shaped die-cut part used to neutralize static electricity generated as paper moves through the printer."),
    ],
  ),
  "mobile": dict(
    title="Mobile Phone", hero="hero.png",
    subtitle="The set of precision die-cut materials that make up a smartphone, from the frame to thermal and protective layers.",
    intro=["Mobile phones have the highest component density among the company's die-cutting applications. Each phone requires dozens of precision die-cut parts, accurate to the millimeter, for bonding, fixing, heat dissipation, dust-proofing and protecting internal components."],
    materials=[
      ("Double-Sided Tape","double-sided-tape.png","Bonds the screen and back cover of the phone."),
      ("Graphite Sheet","graphite.png","Dissipates heat from heat-generating components such as the processor and battery."),
      ("Dust-Proof Net","dust-proof-net.png","Mesh fitted at the speaker/microphone area to keep out dust."),
      ("Protective Film","protective-film.png","Protects the screen/housing surface during assembly and transport."),
      ("Poron Foam","poron.png","Shock-absorbing cushion that seals gaps inside the device."),
      ("Kapton Tape","kapton.png","High-heat-resistant tape used to secure the flexible printed circuit (FPC) inside the device."),
    ],
  ),
  "notebook": dict(
    title="Notebook Computer", hero="hero.png",
    subtitle="Die-cut materials used for assembly, heat dissipation and product identification in laptops.",
    intro=["Inside a laptop is a complex system of components that must be fixed, insulated, thermally managed and protected in the correct position. Precision die-cut products help ensure each component layer is neatly assembled, dissipates heat effectively, and meets brand identification standards."],
    materials=[
      ("PC/PP/PET Sheet","pc-pp-pet.png","Die-cut technical plastic sheet used for decoration and scratch protection of the laptop surface."),
      ("Conductive Foam/Cloth Tape","conductive-foam-cloth-tape.png","Conductive material providing EMI shielding for the circuit board."),
      ("Label","label.png","Labels identifying configuration (chip, operating system, licensing certification, etc.)."),
      ("Copper/Aluminum Foil","copper-aluminum-foil.png","Metal foil providing thermal conduction, electrical conduction and shielding for circuit areas."),
      ("Thermal Conductive Sheet","thermal-conductive-sheet.png","Thermal pad placed between components and the heat sink."),
      ("Double-Sided Tape","double-sided-tape.png","Secures component layers inside the laptop."),
    ],
  ),
  "backlight": dict(
    title="Backlight Module", hero="hero.png",
    subtitle="The precision die-cut optical layers that make up an LCD backlight module.",
    intro=["A backlight module is a stack of optical layers, each performing a specific function: light guiding, diffusion, brightness enhancement, reflection and light blocking. The dimensional accuracy of each die-cut layer directly affects the display quality of the screen."],
    materials=[
      ("Light-Blocking Tape","light-blocking-tape.png","Prevents light from leaking out of the backlight module."),
      ("Reflective Sheet","reflective-sheet.png","Reflects light back to improve lighting efficiency."),
      ("Diffusion Sheet","diffusion-sheet.png","Diffuses light evenly across the screen surface."),
      ("Brightness Enhancement Film","brightness-enhancement-film.png","Enhances brightness level and light uniformity."),
      ("Protective Film","protective-film.png","Protects the surface of optical layers during assembly."),
      ("Foam","foam.png","Shock-absorbing cushion that secures the layers within the backlight module."),
    ],
  ),
  "automobile": dict(
    title="Automobile / Battery", hero="hero.png",
    subtitle="Die-cut materials for interior trim, sound insulation and electric vehicle batteries.",
    intro=["In the automotive and EV battery industry, precision die-cut materials are widely used for interior trim, sound insulation, waterproofing and securing battery packs. Durability, heat resistance and vibration resistance requirements are considerably higher than in typical consumer electronics applications."],
    materials=[
      ("Felt","felt.png","Felt lining for noise reduction and scratch protection in the interior and engine bay."),
      ("Double-Sided Tape","double-sided-tape.png","Bonds vehicle logos and waterproofing components."),
      ("PP/PC/PET Sheet","pp-pc-pet.png","Used for floor mats, headliners, and interior storage boxes."),
      ("Sound-Absorbing Cotton","sound-absorbing-cotton.png","Fitted inside car doors to reduce noise."),
      ("Sponge","sponge.png","Cushioning against vibration and dust at joints."),
      ("Barley Paper","barley-paper.png","Gasket paper used for sealing and thermal insulation at joints."),
    ],
  ),
  "other": dict(
    title="Other Applications", hero=None,
    subtitle="Specialized die-cut materials for electrical cabinets, home appliances and solar energy.",
    intro=["Beyond its core applications, the company also processes many specialized die-cut materials on customer request for industrial electrical cabinets, home appliances, photovoltaic panels and other fields."],
    materials=[
      ("Electrical Cabinet", None, "Labels and insulating materials used in industrial electrical cabinets."),
      ("Silicone Tape","silicone-tape.png","Heat-resistant, residue-free tape used to secure moving parts during transport (e.g. refrigerators)."),
      ("High-Temperature Tape","high-temperature-tape.png","Strong adhesion, heat-resistant and chemical-resistant, used inside electronic devices."),
      ("Energy Efficiency Label","energy-efficiency-label.png","Energy efficiency labels affixed to household electrical appliances."),
      ("PV Panel Edge-Wrapping Tape","pv-edge-tape.png","PET tape used to wrap the edges of photovoltaic panels."),
      ("Sealing Ring","sealing-ring.png","Ring gasket die-cut from silicone/foam, used for sealing and vibration damping."),
      ("Special Tape","special-tape.png","Custom die-cutting of specialty tapes per customer request (phone battery tape, waterproof tape, non-woven face mask material, etc.)."),
    ],
  ),
}

PRODUCT_DETAIL["zh"] = {
  "printer": dict(
    title="打印机/复印机", hero="hero.jpg",
    subtitle="安装在打印机、复印机内部的精密模切材料，支撑设备稳定耐用运行。",
    intro=["打印机与复印机内部机构和电子组件使用了大量精密模切零件：从传感器校准条，到吸墨材料、缓冲垫和除静电毛刷。这些细小部件直接决定设备的运行精度与使用寿命。"],
    materials=[
      ("校准条","calibration-strip.png","用于运行过程中校准打印头/传感器位置，确保打印精度。"),
      ("吸墨棉","ink-absorbing-cotton.jpg","按墨盒形状模切的多孔材料，吸附并保留喷头多余墨水。"),
      ("专用胶带","tape.png","装配过程中用于固定打印机内部零件的专用胶带。"),
      ("压制纸板","pressed-cardboard.png","模切压制纸板，用作支撑框架、绝缘或零件定位。"),
      ("海绵泡棉","foam.png","为打印机内部运动部件提供缓冲、防刮保护。"),
      ("除静电毛刷","electrostatic-brush.png","梳齿状模切部件，用于中和纸张经过打印机时产生的静电。"),
    ],
  ),
  "mobile": dict(
    title="移动电话", hero="hero.png",
    subtitle="构成智能手机的精密模切材料组合，从机身骨架到散热、保护层。",
    intro=["移动电话是公司模切应用中零件密度最高的电子产品。每部手机需要数十种精密到毫米级的模切零件，用于粘贴固定、散热、防尘及保护内部元件。"],
    materials=[
      ("双面胶","double-sided-tape.png","粘贴固定手机屏幕与后盖。"),
      ("石墨散热片","graphite.png","为处理器、电池等发热元件散热。"),
      ("防尘网","dust-proof-net.png","安装于听筒/麦克风区域，防止灰尘进入。"),
      ("保护膜","protective-film.png","在装配及运输过程中保护屏幕/外壳表面。"),
      ("Poron泡棉","poron.png","缓冲减震，密封机身内部间隙。"),
      ("Kapton胶带","kapton.png","耐高温胶带，用于固定机身内部的软性电路板（FPC）。"),
    ],
  ),
  "notebook": dict(
    title="笔记本电脑", hero="hero.png",
    subtitle="用于笔记本电脑装配、散热及产品标识的模切材料。",
    intro=["笔记本电脑内部是一套复杂的元件系统，需要精确固定、绝缘、导热并加以保护。精密模切产品确保每一层元件整齐装配、有效散热，并符合品牌标识规范。"],
    materials=[
      ("PC/PP/PET板材","pc-pp-pet.png","模切工程塑料板材，用于机身表面装饰及防刮。"),
      ("导电泡棉/导电布","conductive-foam-cloth-tape.png","为主板提供导电及电磁屏蔽（EMI）功能。"),
      ("标签","label.png","标识配置信息（芯片、操作系统、授权认证等）的标签。"),
      ("铜箔/铝箔","copper-aluminum-foil.png","为电路区域提供导热、导电及屏蔽功能的金属箔材。"),
      ("导热片","thermal-conductive-sheet.png","安装于元件与散热器之间的导热片。"),
      ("双面胶","double-sided-tape.png","固定笔记本电脑内部各层元件。"),
    ],
  ),
  "backlight": dict(
    title="背光模组", hero="hero.png",
    subtitle="构成LCD背光模组的精密模切光学膜层。",
    intro=["背光模组由多层光学材料叠加构成，每一层各司其职：导光、扩散、增亮、反射及遮光。每层模切材料的尺寸精度直接影响屏幕的显示效果。"],
    materials=[
      ("遮光胶带","light-blocking-tape.png","防止光线从背光模组外泄。"),
      ("反射片","reflective-sheet.png","将光线反射回去，提高光利用率。"),
      ("扩散片","diffusion-sheet.png","使光线在屏幕表面均匀扩散。"),
      ("增亮膜（BEF）","brightness-enhancement-film.png","提升亮度及光线均匀度。"),
      ("保护膜","protective-film.png","在装配过程中保护光学膜层表面。"),
      ("泡棉","foam.png","缓冲减震，固定背光模组内的各层材料。"),
    ],
  ),
  "automobile": dict(
    title="汽车/电池", hero="hero.png",
    subtitle="用于内饰、隔音及电动汽车电池的模切材料。",
    intro=["在汽车及电动汽车电池行业，精密模切材料广泛用于内饰、隔音、防水及电池模组固定。其耐久性、耐热性及抗震性要求远高于普通消费电子产品。"],
    materials=[
      ("毛毡","felt.png","用于内饰及发动机舱的隔音、防刮毛毡衬垫。"),
      ("双面胶","double-sided-tape.png","粘贴固定车标及防水部件。"),
      ("PP/PC/PET板材","pp-pc-pet.png","用于地毯、顶棚及内饰收纳盒。"),
      ("吸音棉","sound-absorbing-cotton.png","安装于车门内部，降低噪音。"),
      ("海绵","sponge.png","在连接部位提供防震、防尘缓冲。"),
      ("大麦纸","barley-paper.png","用于连接部位密封及隔热的垫片纸。"),
    ],
  ),
  "other": dict(
    title="其他应用", hero=None,
    subtitle="用于配电柜、家用电器及太阳能领域的特殊模切材料。",
    intro=["除核心应用领域外，公司还根据客户需求为工业配电柜、家用电器、光伏板等领域加工多种特殊模切材料。"],
    materials=[
      ("配电柜", None, "用于工业配电柜的标签及绝缘材料。"),
      ("硅胶胶带","silicone-tape.png","耐高温、无残胶，用于运输过程中固定活动部件（如冰箱）。"),
      ("耐高温胶带","high-temperature-tape.png","粘性强、耐高温、耐化学溶剂，用于电子设备内部。"),
      ("能效标签","energy-efficiency-label.png","粘贴于家用电器上的能效标识标签。"),
      ("光伏板边框封装胶带","pv-edge-tape.png","用于光伏板边框封装的PET胶带。"),
      ("密封圈","sealing-ring.png","以硅胶/泡棉模切而成的密封圈，用于密封及减震。"),
      ("特殊胶带","special-tape.png","根据客户需求模切各类特殊胶带（手机电池胶带、防水胶带、非织造口罩材料等）。"),
    ],
  ),
}

# ---------------- EQUIPMENT (production & testing machines) ----------------
EQUIPMENT_LIST = {}
EQUIPMENT_LIST["vi"] = [
  ("🔧 Máy xẻ rãnh","production","xe-ranh",["Xẻ, chia cuộn vật liệu thành các dải theo kích thước yêu cầu","Mắt điện chỉnh biên, hạn chế lệch biên khi chạy cuộn","Tốc độ 3–10 m/phút, khổ liệu tối đa 1.300 mm"]),
  ("✂️ Máy cắt cuộn","production","cat-cuon",["Dùng dao tròn cắt vật liệu cuộn theo khổ và số lượng cài đặt","Model FCA-1600, công suất 7.5kW, điện áp 380V","Điều khiển qua HMI, có bảng điều khiển phụ khi căn chỉnh"]),
  ("🗜️ Máy cắt khuôn","production","cat-khuon",["Dùng khuôn dao cắt/ép/tạo hình vật liệu cuộn hoặc tấm","Độ chính xác cắt ±0.1mm, tốc độ 10–80 m/phút","Kéo liệu bằng servo motor, PLC+HMI lưu công thức sản xuất"]),
  ("🎞️ Máy cán màng, dán màng","production","can-mang",["Ép/dán các lớp vật liệu bằng lô cán silicone","Bàn làm việc có lỗ hút chân không giữ phẳng vật liệu","Giá cuộn cấp màng và thu màng phế riêng biệt"]),
  ("🎞️ Máy cán màng, dán màng (Model mới)","production","can-mang-new",["Phiên bản mới, tích hợp cụm ép – cán nhiệt","Có dao cắt màng ngay trên dây chuyền","Điều khiển bằng HMI & PLC, cảm biến lực căng màng"]),
  ("🔬 Máy đo VMM (2D)","testing","vmm",["Đo kích thước 2D bằng hình ảnh: điểm, đường, tròn, khoảng cách...","Hiệu chuẩn bằng phương pháp ba vòng tròn chuẩn","Dùng cho QC/IPQC/OQC kiểm tra kích thước sản phẩm"]),
  ("🧪 Máy thử lực kéo – độ bám dính","testing","luc-keo",["Thử kéo, nén, uốn, cắt, xé, bóc tách bằng phần mềm TM2101","Tính tự động lực lớn nhất, lực bóc trung bình, biến dạng lớn nhất","Kiểm tra độ bám dính của tem, màng, băng keo, nhãn, lớp phủ"]),
]
EQUIPMENT_LIST["en"] = [
  ("🔧 Slitting Machine","production","xe-ranh",["Slits roll material into strips at required widths","Edge-correction photoelectric sensor to reduce web drift","Speed 3–10 m/min, maximum material width 1,300 mm"]),
  ("✂️ Roll Cutting Machine","production","cat-cuon",["Uses a circular blade to cut roll material to set width and quantity","Model FCA-1600, 7.5kW power, 380V voltage","HMI-controlled, with an auxiliary panel for blade alignment"]),
  ("🗜️ Die-Cutting Machine","production","cat-khuon",["Uses a die to cut/press/form roll or sheet material","Cutting accuracy ±0.1mm, speed 10–80 m/min","Servo-motor feeding; PLC+HMI stores production recipes"]),
  ("🎞️ Laminating Machine","production","can-mang",["Presses/bonds material layers using a silicone laminating roller","Vacuum-hole worktable keeps material flat","Separate unwind and rewind (waste) stands"]),
  ("🎞️ Laminating Machine (New Model)","production","can-mang-new",["Newer version with an integrated hot-press laminating unit","Built-in film cutting blade on the line","Controlled via HMI & PLC with film tension sensor"]),
  ("🔬 2D Vision Measuring Machine (VMM)","testing","vmm",["Measures 2D dimensions by image: points, lines, circles, distances...","Calibrated using the three-circle calibration method","Used by QC/IPQC/OQC to verify product dimensions"]),
  ("🧪 Tensile / Adhesion Tester","testing","luc-keo",["Tensile, compression, bending, cutting, tearing and peel tests via TM2101 software","Automatically calculates max force, average peel force and max deformation","Tests adhesion of labels, films, tapes and coatings"]),
]
EQUIPMENT_LIST["zh"] = [
  ("🔧 分条机","production","xe-ranh",["将卷状材料按要求尺寸分切成条","纠偏电眼减少材料跑偏","速度3–10米/分钟，最大料宽1,300毫米"]),
  ("✂️ 切卷机","production","cat-cuon",["使用圆刀按设定宽度和数量切割卷状材料","型号FCA-1600，功率7.5kW，电压380V","HMI控制，配备调机用辅助控制面板"]),
  ("🗜️ 模切机","production","cat-khuon",["使用刀模对卷料或片材进行冲切、压合、成型","切割精度±0.1毫米，速度10–80米/分钟","伺服电机送料，PLC+HMI保存生产配方"]),
  ("🎞️ 覆膜、贴合机","production","can-mang",["通过硅胶压辊对材料层进行贴合","真空吸孔工作台保持材料平整","独立的放卷与废料收卷架"]),
  ("🎞️ 覆膜、贴合机（新型号）","production","can-mang-new",["新版本集成热压覆合组","产线上集成切膜刀","采用HMI与PLC控制，配备膜张力传感器"]),
  ("🔬 VMM影像测量仪（2D）","testing","vmm",["以影像方式测量2D尺寸：点、线、圆、距离等","采用三圆校正法进行校准","供QC/IPQC/OQC用于产品尺寸检验"]),
  ("🧪 拉力/附着力试验机","testing","luc-keo",["通过TM2101软件进行拉伸、压缩、弯曲、剪切、撕裂及剥离测试","自动计算最大力、平均剥离力及最大变形","用于检测标签、薄膜、胶带及涂层的附着力"]),
]

EQUIPMENT_DETAIL = {}
EQUIPMENT_DETAIL["vi"] = {
  "xe-ranh": dict(
    doc_code="PWI-001", title="Máy xẻ rãnh", hero="hero.jpg",
    subtitle="Thiết bị xẻ, chia cuộn vật liệu thành các dải theo kích thước yêu cầu, dùng trong công đoạn phân chia nguyên liệu trước khi cắt bế.",
    intro=["Máy xẻ rãnh dùng để xẻ cuộn vật liệu đầu vào thành nhiều dải nhỏ theo đúng kích thước kỹ thuật, phục vụ cho các công đoạn gia công tiếp theo. Máy được trang bị mắt điện chỉnh biên giúp hạn chế lệch biên, cùng hệ thống điều chỉnh lực căng (tension) đảm bảo cuộn vật liệu ra thẳng, đều và ổn định."],
    specs=[("Chiều rộng nguyên liệu tối đa","1.300 mm"),("Đường kính nạp liệu tối đa","Ø600 mm"),("Đường kính thu liệu tối đa","Ø450 mm"),("Tốc độ máy","3 – 10 m/phút"),("Nguồn điện","AC 380V, 3P, 50/60Hz"),("Khí nén yêu cầu","0.6 – 0.8 MPa")],
    structure=["Trục nạp liệu (A) và giá đỡ trục nạp liệu","Con lăn dẫn hướng, con lăn cao su ép","Cụm lưỡi xẻ (dao xẻ) – khu vực nguy hiểm cao","Trục thu liệu (B), mắt điện chỉnh biên","Bảng điều khiển và hộp điện (tủ điện)","Chân đế giảm chấn (đệm cao su)"],
    safety="Nguyên tắc đỏ: khi máy đang chạy, nghiêm cấm đưa tay, tóc, quần áo, găng tay, dây đeo thẻ hoặc bất kỳ dụng cụ nào vào khu vực con lăn, trục quay và dao xẻ.",
  ),
  "cat-cuon": dict(
    doc_code="PWI-002", title="Máy cắt cuộn", hero="hero.jpg",
    subtitle="Thiết bị sử dụng dao tròn cắt vật liệu dạng cuộn theo khổ rộng và số lượng đã cài đặt.",
    intro=["Máy cắt cuộn (model FCA-1600) dùng dao tròn để cắt vật liệu dạng cuộn thành các đoạn/cuộn nhỏ theo khổ rộng và số lượng yêu cầu của lệnh sản xuất. Máy được điều khiển qua màn hình cảm ứng HMI, có bảng điều khiển phụ hỗ trợ căn chỉnh khi lên dao mới hoặc đổi khổ cắt."],
    specs=[("Model","FCA-1600"),("Công suất","7.5 kW"),("Điện áp","380V"),("Kích thước máy (D×R×C)","3.460 × 1.380 × 1.710 mm")],
    structure=["Tủ điều khiển chính (HMI + nút điều khiển)","Cụm dao cắt tròn và vùng kẹp – khu vực nguy hiểm cao","Bảng điều khiển phụ dùng khi căn chỉnh","Trục vật liệu và đầu đỡ phôi"],
    safety="Dao tròn sắc, quay tốc độ cao có thể gây cắt đứt tay hoặc bắn mảnh vật liệu/dao; trục cuộn đang quay có thể cuốn tay áo, tóc, găng tay gây kẹp kéo. Phải che chắn đầy đủ, không đưa tay vào, tắt nguồn khi căn dao và chỉ dùng găng chống cắt đúng lúc.",
  ),
  "cat-khuon": dict(
    doc_code="PWI-003", title="Máy cắt khuôn", hero="hero.jpg",
    subtitle="Thiết bị dùng khuôn dao để cắt, ép, tạo hình vật liệu dạng cuộn hoặc dạng tấm — công đoạn cắt bế chính xác cốt lõi của nhà máy.",
    intro=["Máy cắt khuôn là thiết bị trung tâm trong công đoạn cắt bế chính xác, sử dụng khuôn dao được thiết kế theo biên dạng sản phẩm để cắt, ép và tạo hình vật liệu. Máy tích hợp điều khiển PLC + HMI cho phép cài đặt thông số nhanh và lưu công thức sản xuất, cùng hệ thống kéo liệu bằng servo motor đảm bảo độ chính xác cắt cao và cảm biến giám sát lệch biên, hết liệu, kẹt liệu, quá tải."],
    specs=[("Khổ liệu tối đa","350 mm"),("Đường kính cuộn cấp tối đa","Ø500 mm"),("Đường kính cuộn thu tối đa","Ø400 mm"),("Tốc độ máy","10 – 80 m/phút"),("Độ chính xác cắt","±0.1 mm"),("Điện áp","380V – 50Hz – 3P"),("Công suất","4.0 kW"),("Khí nén yêu cầu","0.5 – 0.7 MPa"),("Kích thước máy (D×R×C)","1.900 × 900 × 1.500 mm"),("Trọng lượng","~450 kg")],
    structure=["Bảng điều khiển HMI + nút điều khiển","Trục cấp liệu (unwinder)","Con lăn căng liệu và bộ điều chỉnh biên liệu","Cụm bế/ép (die-cut/press) – khuôn dao thay nhanh","Bộ kéo liệu bằng servo motor (servo feeder)","Bộ thu liệu và khay thu sản phẩm","Chân đế chống rung (đệm cao su)"],
    safety="Người vận hành phải nhận biết đúng các cụm chính trước khi thao tác; không điều chỉnh hoặc tháo che chắn khi máy đang vận hành.",
  ),
  "can-mang": dict(
    doc_code="PWI-004", title="Máy cán màng, dán màng", hero="hero.jpg",
    subtitle="Thiết bị ép/dán các lớp vật liệu dạng cuộn bằng lô cán (silicone), phục vụ công đoạn phủ, bảo vệ hoặc ghép lớp vật liệu.",
    intro=["Máy cán màng, dán màng dùng để ép hoặc dán các lớp vật liệu (màng, băng keo hai mặt, màng bảo vệ...) lên bề mặt sản phẩm thông qua lô cán silicone, đảm bảo độ phẳng, độ bám dính đồng đều, không nhăn và không bong sau khi cán."],
    specs=[],
    structure=["Giá cuộn cấp màng (Unwind)","Cụm căng màng","Trục dẫn hướng màng","Cụm cán màng (lô silicone)","Cụm ép màng","Bàn làm việc có lỗ hút chân không","Giá cuộn thu màng (Rewind)","Bảng điều khiển chính và tủ điện"],
    safety="Không đưa tay vào điểm kẹp giữa các lô khi máy đang chạy; không kéo màng bằng tay khi trục còn quay. Trước khi vệ sinh sâu, tháo lắp lô hoặc xử lý kẹt vật liệu phải dừng máy, tắt nguồn.",
  ),
  "can-mang-new": dict(
    doc_code="PWI-005", title="Máy cán màng, dán màng (Model mới)", hero="hero.jpg",
    subtitle="Phiên bản máy cán màng/dán màng thế hệ mới, bổ sung cụm ép - cán nhiệt và dao cắt màng tích hợp.",
    intro=["Đây là phiên bản máy cán màng, dán màng thế hệ mới được trang bị thêm cụm ép - cán nhiệt (gia nhiệt khi cán) và dao cắt màng tích hợp ngay trên dây chuyền, giúp rút ngắn công đoạn so với model cũ. Máy vận hành thông qua bộ điều khiển HMI & PLC, có cảm biến lực căng giữ ổn định quá trình chạy màng."],
    specs=[],
    structure=["Trục cấp màng","Cảm biến/lực căng màng","Dẫn hướng màng","Cụm ép - cán nhiệt","Dao cắt màng","Bàn ra sản phẩm","Động cơ truyền động","Trục cuốn màng phế","HMI & PLC"],
    safety="Không đeo găng vải lỏng, trang sức, dây đeo hoặc quần áo rộng khi thao tác gần lô cán và trục quay; không đưa tay vào điểm kẹp giữa các lô khi máy đang chạy.",
  ),
  "vmm": dict(
    doc_code="QWI-001", title="Máy đo VMM (2D)", hero="hero.jpg",
    subtitle="Máy đo lường bằng hình ảnh (Vision Measuring Machine) dùng để kiểm tra kích thước 2D của sản phẩm cắt bế với độ chính xác cao.",
    intro=["Máy đo VMM (Vision Measuring Machine) 2D là thiết bị đo lường không tiếp xúc, sử dụng camera và phần mềm đo ảnh chuyên dụng để xác định kích thước điểm, đường, tròn, cung tròn, ellipse, chữ nhật, rãnh, khoảng cách, tọa độ và dung sai của sản phẩm. Đây là thiết bị kiểm tra chất lượng chủ lực tại phòng QC/IPQC/OQC, đảm bảo kết quả đo chính xác và có thể truy xuất."],
    specs=[("Phần mềm đo","LT-3D / 2D VMM"),("Phương pháp hiệu chuẩn","Ba vòng tròn chuẩn (3 circles)"),("Nguồn điện","220V, 50-60Hz, có tiếp đất"),("Nhiệt độ môi trường khuyến nghị","20°C - 25°C")],
    structure=["Bàn máy đo và hệ trục X/Y/Z","Ống kính, đèn chiếu sáng trên/dưới","Joystick/chuột điều khiển chuyển động trục","Nút nguồn và nút dừng khẩn cấp","Máy tính và phần mềm đo ảnh"],
    safety="Chỉ người đã được đào tạo về máy, phần mềm đo và kiến thức đo lường cơ bản mới được vận hành; không tự ý tháo, điều chỉnh linh kiện hoặc dùng phụ kiện không chính hãng; tránh đặt máy gần nguồn rung, tủ điện công suất lớn hoặc nơi nhiều bụi/ẩm.",
  ),
  "luc-keo": dict(
    doc_code="QWI-003", title="Máy thử lực kéo - độ bám dính", hero="hero.jpg",
    subtitle="Thiết bị thử kéo/nén/xé/bóc tách dùng phần mềm TM2101, kiểm tra độ bám dính và độ bền của tem, màng, băng keo, nhãn, lớp phủ.",
    intro=["Máy thử lực kéo - độ bám dính sử dụng phần mềm điều khiển TM2101, có khả năng thực hiện các phép thử kéo, nén, uốn, cắt, xé và bóc tách. Phần mềm thu thập, lưu trữ, xử lý và in kết quả, tự động tính lực lớn nhất, lực bóc trung bình và biến dạng lớn nhất - phục vụ kiểm tra độ bám dính của tem, màng, băng keo (tape), nhãn và lớp phủ trước khi xuất xưởng."],
    specs=[("Phần mềm điều khiển","TM2101 / TestMaster"),("Phép thử hỗ trợ","Kéo, nén, uốn, cắt, xé, bóc tách"),("Điều kiện làm việc tham khảo","0 - 55°C, độ ẩm tương đối < 85%"),("Nguồn điện","220V ±10% AC, 50Hz")],
    structure=["Ngàm kẹp mẫu trên/dưới","Cảm biến lực (load cell)","Bảng điều khiển tốc độ và hành trình","Máy tính và phần mềm TM2101/TestMaster"],
    safety="Không đưa tay vào giữa ngàm kẹp hoặc cơ cấu chuyển động khi máy đang bật/chạy; đeo kính bảo hộ khi mẫu có khả năng đứt, văng, bật ngược; nút Stop/F4 và dừng khẩn cấp phải luôn hoạt động và trong tầm với.",
  ),
}
print("EQUIPMENT VI ok")

EQUIPMENT_DETAIL["en"] = {
  "xe-ranh": dict(
    doc_code="PWI-001", title="Slitting Machine", hero="hero.jpg",
    subtitle="Equipment that slits roll material into strips at the required dimensions, used to divide raw material before die-cutting.",
    intro=["The slitting machine slits incoming roll material into multiple narrow strips to the exact technical dimensions required for downstream processing. It is equipped with an edge-correction photoelectric sensor to limit web drift, along with a tension control system that keeps the material running straight, even and stable."],
    specs=[("Maximum material width","1,300 mm"),("Maximum unwind diameter","O600 mm"),("Maximum rewind diameter","O450 mm"),("Machine speed","3 - 10 m/min"),("Power supply","AC 380V, 3P, 50/60Hz"),("Required compressed air","0.6 - 0.8 MPa")],
    structure=["Feed shaft (A) and feed shaft stand","Guide rollers, rubber pressure roller","Slitting blade assembly - high-risk zone","Rewind shaft (B), edge-correction sensor","Control panel and electrical cabinet","Vibration-damping feet (rubber pads)"],
    safety="Red-line rule: while the machine is running, it is strictly forbidden to put hands, hair, clothing, gloves, lanyards or any tool into the roller, shaft or blade area.",
  ),
  "cat-cuon": dict(
    doc_code="PWI-002", title="Roll Cutting Machine", hero="hero.jpg",
    subtitle="Equipment using a circular blade to cut roll material to a set width and quantity.",
    intro=["The roll cutting machine (model FCA-1600) uses a circular blade to cut roll material into shorter rolls/lengths according to the width and quantity specified in the production order. It is controlled via an HMI touchscreen and includes an auxiliary control panel to assist alignment when installing a new blade or changing the cutting width."],
    specs=[("Model","FCA-1600"),("Power","7.5 kW"),("Voltage","380V"),("Machine dimensions (LxWxH)","3,460 x 1,380 x 1,710 mm")],
    structure=["Main control cabinet (HMI + control buttons)","Circular blade assembly and clamping zone - high-risk area","Auxiliary control panel used for alignment","Material shaft and support head"],
    safety="The sharp, high-speed rotating circular blade can cut hands or eject material/blade fragments; the rotating roll shaft can catch sleeves, hair or gloves causing entanglement. Guards must be fully in place, hands must not be inserted, power must be off when adjusting the blade, and cut-resistant gloves used only when appropriate.",
  ),
  "cat-khuon": dict(
    doc_code="PWI-003", title="Die-Cutting Machine", hero="hero.jpg",
    subtitle="Equipment using a die to cut, press and form roll or sheet material - the core precision die-cutting step of the factory.",
    intro=["The die-cutting machine is the central equipment in the precision die-cutting process, using a die designed to the product's contour to cut, press and form material. It integrates PLC + HMI control for quick parameter setup and recipe storage, together with a servo-motor feed system that ensures high cutting accuracy and sensors that monitor web drift, material shortage, jamming and overload."],
    specs=[("Maximum material width","350 mm"),("Maximum unwind diameter","O500 mm"),("Maximum rewind diameter","O400 mm"),("Machine speed","10 - 80 m/min"),("Cutting accuracy","±0.1 mm"),("Voltage","380V - 50Hz - 3P"),("Power","4.0 kW"),("Required compressed air","0.5 - 0.7 MPa"),("Machine dimensions (LxWxH)","1,900 x 900 x 1,500 mm"),("Weight","~450 kg")],
    structure=["HMI control panel + control buttons","Feed shaft (unwinder)","Tension roller and edge-adjustment unit","Die-cut/press unit - quick die change","Servo-motor feeder","Take-up unit and output tray","Anti-vibration feet (rubber pads)"],
    safety="Operators must correctly identify the main assemblies before operating; guards must not be adjusted or removed while the machine is running.",
  ),
  "can-mang": dict(
    doc_code="PWI-004", title="Laminating Machine", hero="hero.jpg",
    subtitle="Equipment that presses/bonds roll material layers using a silicone laminating roller, used for coating, protecting or combining material layers.",
    intro=["The laminating machine presses or bonds material layers (film, double-sided tape, protective film, etc.) onto the product surface using a silicone laminating roller, ensuring flatness and uniform adhesion without wrinkling or lifting after lamination."],
    specs=[],
    structure=["Film unwind stand","Film tensioning unit","Film guide shaft","Laminating unit (silicone roller)","Pressing unit","Vacuum-hole worktable","Film rewind stand","Main control panel and electrical cabinet"],
    safety="Do not put hands into the nip point between rollers while the machine is running; do not pull film by hand while the shaft is still turning. Before deep cleaning, removing rollers, or clearing jammed material, the machine must be stopped and powered off.",
  ),
  "can-mang-new": dict(
    doc_code="PWI-005", title="Laminating Machine (New Model)", hero="hero.jpg",
    subtitle="A newer-generation laminating machine adding an integrated hot-press laminating unit and built-in film cutting blade.",
    intro=["This newer-generation laminating machine adds a hot-press laminating unit (heat applied during lamination) and a film-cutting blade built directly into the line, shortening the process compared with the older model. It operates via an HMI & PLC controller with a tension sensor that keeps the film running stable."],
    specs=[],
    structure=["Film feed shaft","Film tension sensor","Film guide","Hot-press laminating unit","Film cutting blade","Output table","Drive motor","Waste film take-up shaft","HMI & PLC"],
    safety="Do not wear loose fabric gloves, jewelry, lanyards or loose clothing when working near the laminating roller and rotating shaft; do not put hands into the nip point between rollers while the machine is running.",
  ),
  "vmm": dict(
    doc_code="QWI-001", title="2D Vision Measuring Machine (VMM)", hero="hero.jpg",
    subtitle="A Vision Measuring Machine used to inspect the 2D dimensions of die-cut products with high accuracy.",
    intro=["The 2D Vision Measuring Machine (VMM) is a non-contact measurement instrument that uses a camera and dedicated image-measurement software to determine points, lines, circles, arcs, ellipses, rectangles, grooves, distances, coordinates and tolerances of a product. It is the primary quality-inspection instrument in the QC/IPQC/OQC department, ensuring accurate, traceable measurement results."],
    specs=[("Measurement software","LT-3D / 2D VMM"),("Calibration method","Three-circle calibration"),("Power supply","220V, 50-60Hz, properly grounded"),("Recommended ambient temperature","20°C - 25°C")],
    structure=["Measuring stage and X/Y/Z axis system","Lens, upper/lower illumination lights","Joystick/mouse for axis movement control","Power button and emergency stop button","Computer and image-measurement software"],
    safety="Only personnel trained on the machine, measurement software and basic metrology knowledge may operate it; do not disassemble or adjust components, or use non-original accessories, without authorization; keep the machine away from vibration sources, high-power electrical cabinets, or dusty/humid areas.",
  ),
  "luc-keo": dict(
    doc_code="QWI-003", title="Tensile / Adhesion Tester", hero="hero.jpg",
    subtitle="A tensile/compression/tear/peel testing machine using TM2101 software to check the adhesion and durability of labels, films, tapes and coatings.",
    intro=["The tensile/adhesion tester uses TM2101 control software and can perform tensile, compression, bending, cutting, tearing and peel tests. The software collects, stores, processes and prints results, automatically calculating maximum force, average peel force and maximum deformation - used to verify the adhesion of labels, films, tapes and coatings before products leave the factory."],
    specs=[("Control software","TM2101 / TestMaster"),("Supported tests","Tensile, compression, bending, cutting, tearing, peeling"),("Reference operating conditions","0 - 55°C, relative humidity < 85%"),("Power supply","220V ±10% AC, 50Hz")],
    structure=["Upper/lower sample clamps","Load cell (force sensor)","Speed and stroke control panel","Computer with TM2101/TestMaster software"],
    safety="Do not put hands between the clamps or moving mechanism while the machine is powered on/running; wear safety glasses when the sample may break, fly off or spring back; the Stop/F4 button and emergency stop must always be functional and within reach.",
  ),
}
print("EQUIPMENT EN ok")

EQUIPMENT_DETAIL["zh"] = {
  "xe-ranh": dict(
    doc_code="PWI-001", title="分条机", hero="hero.jpg",
    subtitle="用于将卷状材料按要求尺寸分切成条的设备，用于模切前的原料分切工序。",
    intro=["分条机用于将进料卷材按技术尺寸要求分切成多条窄幅材料，供后续加工工序使用。设备配备纠偏电眼以减少跑偏，并配有张力控制系统，确保材料运行平直、均匀、稳定。"],
    specs=[("最大原料宽度","1,300毫米"),("最大放料直径","O600毫米"),("最大收料直径","O450毫米"),("设备速度","3-10米/分钟"),("电源","AC 380V，3相，50/60Hz"),("所需气压","0.6-0.8 MPa")],
    structure=["放料轴（A）及放料轴支架","导向辊、橡胶压辊","分切刀组--高风险区域","收料轴（B）、纠偏电眼","控制面板及电控箱","减震脚（橡胶垫）"],
    safety="红线原则：设备运行时，严禁将手、头发、衣服、手套、证件挂绳或任何工具伸入滚轴、转轴及分切刀区域。",
  ),
  "cat-cuon": dict(
    doc_code="PWI-002", title="切卷机", hero="hero.jpg",
    subtitle="使用圆刀按设定宽度和数量切割卷状材料的设备。",
    intro=["切卷机（型号FCA-1600）使用圆刀将卷状材料按工单要求的宽度和数量切割成小卷/短段。设备通过HMI触摸屏控制，并配有辅助控制面板，便于更换新刀或调整切割宽度时进行调机。"],
    specs=[("型号","FCA-1600"),("功率","7.5 kW"),("电压","380V"),("设备尺寸（长x宽x高）","3,460 x 1,380 x 1,710 毫米")],
    structure=["主控制柜（HMI+控制按钮）","圆刀组件及夹卷区--高风险区域","调机用辅助控制面板","主轴及托料座"],
    safety="高速旋转的锋利圆刀可能割伤手部或飞溅材料/刀具碎片；旋转中的卷轴可能卷入衣袖、头发或手套导致夹伤。必须做好防护，不得伸手，调刀时须断电，仅在适当时机使用防割手套。",
  ),
  "cat-khuon": dict(
    doc_code="PWI-003", title="模切机", hero="hero.jpg",
    subtitle="使用刀模对卷料或片材进行冲切、压合、成型的设备--工厂精密模切的核心工序。",
    intro=["模切机是精密模切工序的核心设备，使用按产品外形设计的刀模对材料进行冲切、压合与成型。设备集成PLC+HMI控制，可快速设定参数并保存生产配方，配合伺服电机送料系统确保高切割精度，并配备跑偏、缺料、卡料、过载监控传感器。"],
    specs=[("最大料宽","350毫米"),("最大放卷直径","O500毫米"),("最大收卷直径","O400毫米"),("设备速度","10-80米/分钟"),("切割精度","±0.1毫米"),("电压","380V-50Hz-3相"),("功率","4.0 kW"),("所需气压","0.5-0.7 MPa"),("设备尺寸（长x宽x高）","1,900 x 900 x 1,500 毫米"),("重量","约450公斤")],
    structure=["HMI控制面板及控制按钮","放料轴（Unwinder）","张力辊及纠偏调整机构","模切/压合组件--刀模可快速更换","伺服电机送料机构","收料机构及成品收集盘","防震底座（橡胶垫）"],
    safety="操作人员在操作前必须正确识别主要部件；设备运行中不得调整或拆除防护装置。",
  ),
  "can-mang": dict(
    doc_code="PWI-004", title="覆膜、贴合机", hero="hero.jpg",
    subtitle="通过硅胶压辊对卷状材料层进行压合/贴合的设备，用于覆膜、保护或复合材料层。",
    intro=["覆膜、贴合机通过硅胶压辊将材料层（膜材、双面胶、保护膜等）压合或贴合到产品表面，确保贴合后平整、粘合均匀，不起皱、不脱胶。"],
    specs=[],
    structure=["放料架（Unwind）","张力控制组","导膜辊","覆膜组件（硅胶压辊）","压合组件","真空吸孔工作台","收膜架（Rewind）","主控制面板及电控柜"],
    safety="设备运行时严禁将手伸入压辊夹点；轴仍在转动时不得用手拉膜。深度清洁、拆装压辊或处理卡料前，必须停机断电。",
  ),
  "can-mang-new": dict(
    doc_code="PWI-005", title="覆膜、贴合机（新型号）", hero="hero.jpg",
    subtitle="新一代覆膜/贴合机型号，新增热压覆合组及集成式切膜刀。",
    intro=["此为新一代覆膜、贴合机型号，新增了热压覆合组（贴合时加热）以及产线上直接集成的切膜刀，相比旧型号缩短了作业工序。设备通过HMI与PLC控制器运行，配备张力传感器以保持贴膜过程稳定。"],
    specs=[],
    structure=["放料轴","张力传感器","导膜组","热压覆合组","切膜刀","出料台","传动电机","废膜收卷轴","HMI与PLC"],
    safety="靠近压辊和旋转轴操作时，不得佩戴宽松布手套、饰品、吊绳或宽松衣物；设备运行时严禁将手伸入压辊夹点。",
  ),
  "vmm": dict(
    doc_code="QWI-001", title="VMM影像测量仪（2D）", hero="hero.jpg",
    subtitle="影像测量仪（Vision Measuring Machine），用于高精度检测模切产品的2D尺寸。",
    intro=["2D影像测量仪（VMM）是一种非接触式测量设备，通过相机及专用影像测量软件确定产品的点、线、圆、圆弧、椭圆、矩形、槽、距离、坐标及公差等尺寸。它是QC/IPQC/OQC部门的主力检测设备，确保测量结果准确、可追溯。"],
    specs=[("测量软件","LT-3D / 2D VMM"),("校准方法","三圆校正法"),("电源","220V，50-60Hz，须良好接地"),("建议环境温度","20°C - 25°C")],
    structure=["测量工作台及X/Y/Z轴系统","镜头、上/下光源","摇杆/鼠标控制轴移动","电源按钮及急停按钮","计算机及影像测量软件"],
    safety="只有经过设备、测量软件及基本计量知识培训的人员方可操作；不得擅自拆卸、调整零部件或使用非原厂配件；避免将设备放置于振动源、强电柜或多尘潮湿环境附近。",
  ),
  "luc-keo": dict(
    doc_code="QWI-003", title="拉力/附着力试验机", hero="hero.jpg",
    subtitle="使用TM2101软件的拉伸/压缩/撕裂/剥离试验设备，用于检测标签、薄膜、胶带、标贴及涂层的附着力与强度。",
    intro=["拉力/附着力试验机采用TM2101控制软件，可执行拉伸、压缩、弯曲、剪切、撕裂及剥离测试。软件可采集、保存、处理并打印结果，自动计算最大力、平均剥离力及最大变形--用于产品出货前检测标签、薄膜、胶带及涂层的附着力。"],
    specs=[("控制软件","TM2101 / TestMaster"),("支持测试类型","拉伸、压缩、弯曲、剪切、撕裂、剥离"),("参考工作条件","0-55°C，相对湿度<85%"),("电源","220V ±10% AC，50Hz")],
    structure=["上/下夹具","力传感器（Load Cell）","速度及行程控制面板","计算机及TM2101/TestMaster软件"],
    safety="设备通电或运行时严禁将手伸入夹具或运动机构；样品可能断裂、飞溅或回弹时须佩戴护目镜；Stop/F4及急停按钮必须始终有效且在可触及范围内。",
  ),
}
print("EQUIPMENT ZH ok")

PAGE_FILES = {"index":"index.html","about":"about.html","products":"products.html","equipment":"equipment.html","quality-hse":"quality-hse.html","contact":"contact.html"}

def header(lang, active_page, depth=0, lang_target_path=None):
    d = C[lang]
    nav_prefix = "../"*depth
    root_prefix = "../"*(depth+1)
    nav_hrefs = [nav_prefix+f for f in PAGE_FILES.values()]
    nav_html = ""
    for i, label in enumerate(d["nav"]):
        page_key = list(PAGE_FILES.keys())[i]
        cls = ' class="active"' if page_key == active_page else ""
        nav_html += f'<li><a href="{nav_hrefs[i]}"{cls}>{label}</a></li>\n'
    lang_html = ""
    for lg in LANGS:
        cls = ' class="active"' if lg == lang else ""
        if lang_target_path:
            target = root_prefix + f"{lg}/{lang_target_path[lg]}"
        else:
            target = root_prefix + f"{lg}/{PAGE_FILES[active_page]}"
        lang_html += f'<a href="{target}"{cls}>{LANG_LABEL[lg]}</a>'
    return f"""<header>
  <div class="container nav-wrap">
    <a href="{nav_prefix}index.html" class="logo">
      <img src="{root_prefix}assets/logo.png" alt="YMX" class="logo-img">
      <div class="logo-text">
        <strong>{d['site_name']}</strong>
        <span>{d['site_tag']}</span>
      </div>
    </a>
    <div class="nav-toggle" id="navToggle"><span></span><span></span><span></span></div>
    <div class="nav-area" id="navMenu">
      <nav><ul>
        {nav_html}
      </ul></nav>
      <div class="lang-switch">{lang_html}</div>
    </div>
  </div>
</header>
"""

def footer(lang, depth=0):
    d = C[lang]
    root_prefix = "../"*(depth+1)
    return f"""<footer>
  <div class="container">
    <div class="footer-inner">
      <div class="logo">
        <img src="{root_prefix}assets/logo.png" alt="YMX" class="logo-img">
        <div class="logo-text">
          <strong style="color:#fff;">{d['site_name']} {d['site_tag']}</strong>
        </div>
      </div>
      <div>{d['copyright']}</div>
    </div>
    <p class="footer-legal">{d['footer_legal']}</p>
  </div>
</footer>
<script src="{root_prefix}assets/nav.js"></script>
"""

def page_shell(lang, active_page, body, depth=0, lang_target_path=None):
    d = C[lang]
    root_prefix = "../"*(depth+1)
    return f"""<!DOCTYPE html>
<html lang="{HTML_LANG[lang]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d['meta_title']}</title>
<meta name="description" content="{d['meta_desc']}">
<link rel="stylesheet" href="{root_prefix}assets/style.css">
<link rel="icon" type="image/svg+xml" href="{root_prefix}assets/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="{root_prefix}assets/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{root_prefix}assets/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="{root_prefix}assets/apple-touch-icon.png">
<link rel="manifest" href="{root_prefix}site.webmanifest">
<meta name="theme-color" content="#0b2a4a">
</head>
<body>
{header(lang, active_page, depth, lang_target_path)}
{body}
{footer(lang, depth)}
</body>
</html>
"""

def build_index(lang):
    d = C[lang]
    stats_html = "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v,l in d["stats"])
    values_html = "".join(f'''<div class="value-card">
        <div class="value-icon">{icon}</div>
        <h4>{title}</h4>
        <p>{desc}</p>
      </div>''' for icon,title,desc in d["values"])
    body = f"""
<section class="hero">
  <div class="container hero-inner">
    <span class="eyebrow" style="color:#ffcf5c;">{d['hero_eyebrow']}</span>
    <h1>{d['hero_pre']}<em>{d['hero_em']}</em>{d['hero_post']}</h1>
    <p>{d['hero_sub']}</p>
    <div class="btn-row">
      <a href="contact.html" class="btn btn-primary">{d['cta1']}</a>
      <a href="about.html" class="btn btn-outline">{d['cta2']}</a>
    </div>
  </div>
  <div class="container hero-stats">
    {stats_html}
  </div>
</section>

<section>
  <div class="container">
    <span class="eyebrow">{d['home_intro_eyebrow']}</span>
    <h2 class="section-title">{d['home_intro_title']}</h2>
    <p class="section-sub" style="max-width:900px;">{d['home_intro_text']} <a href="about.html" style="color:var(--blue);font-weight:700;">{d['home_intro_link']}</a></p>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <span class="eyebrow">{d['values_eyebrow']}</span>
    <h2 class="section-title">{d['values_title']}</h2>
    <p class="section-sub">{d['values_sub']}</p>
    <div class="values-grid">
      {values_html}
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-banner">
      <h3>{d['cta_banner_title']}</h3>
      <a href="contact.html" class="btn btn-primary">{d['cta_banner_btn']}</a>
    </div>
  </div>
</section>
"""
    return page_shell(lang, "index", body)

def build_about(lang):
    d = C[lang]
    paras_html = "".join(f"<p>{p}</p>" for p in d["about_paras"])
    rows_html = "".join(f'<div class="info-row"><span class="k">{k}</span><span class="v">{v}</span></div>' for k,v in d["legal_rows"])
    tl_html = ""
    for i,(y,l) in enumerate(d["timeline"]):
        cls = " vn" if i == len(d["timeline"])-1 else ""
        tl_html += f'<div class="tl-item{cls}"><b>{y}</b><span>{l}</span></div>'
    body = f"""
<section class="page-banner">
  <div class="container">
    <span class="eyebrow" style="color:#ffcf5c;">{d['about_eyebrow']}</span>
    <h1>{d['about_title']}</h1>
    <p>{d['about_sub']}</p>
  </div>
</section>

<section>
  <div class="container about-grid">
    <div>
      {paras_html}
    </div>
    <div class="info-card">
      <h4>{d['legal_title']}</h4>
      {rows_html}
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <span class="eyebrow">{d['timeline_eyebrow']}</span>
    <h2 class="section-title">{d['timeline_title']}</h2>
    <p class="section-sub">{d['timeline_sub']}</p>
    <div class="timeline">
      {tl_html}
    </div>
  </div>
</section>
"""
    return page_shell(lang, "about", body)

def build_products(lang):
    d = C[lang]
    strengths_html = ""
    for i,(t,desc) in enumerate(d["strengths"]):
        strengths_html += f'''<div class="strength-card">
        <div class="num">0{i+1}</div>
        <h4>{t}</h4>
        <p>{desc}</p>
      </div>'''
    apps_html = ""
    for title, items, slug in d["apps"]:
        items_html = "".join(f"<li>{it}</li>" for it in items)
        apps_html += f'''<a class="app-card" href="products/{slug}.html">
        <div class="app-head"><h4>{title}</h4></div>
        <div class="app-body"><ul>{items_html}</ul>
          <div class="app-link">{d['product_detail_link']}</div>
        </div>
      </a>'''
    body = f"""
<section class="page-banner">
  <div class="container">
    <span class="eyebrow" style="color:#ffcf5c;">{d['products_eyebrow']}</span>
    <h1>{d['products_title']}</h1>
    <p>{d['products_sub']}</p>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <span class="eyebrow">{d['strengths_eyebrow']}</span>
    <h2 class="section-title">{d['strengths_title']}</h2>
    <p class="section-sub">{d['strengths_sub']}</p>
    <div class="strength-grid">
      {strengths_html}
    </div>
  </div>
</section>

<section>
  <div class="container">
    <span class="eyebrow">{d['apps_eyebrow']}</span>
    <h2 class="section-title">{d['apps_title']}</h2>
    <p class="section-sub">{d['apps_sub']}</p>
    <div class="app-grid">
      {apps_html}
    </div>
  </div>
</section>
"""
    return page_shell(lang, "products", body)

def build_equipment(lang):
    d = C[lang]
    items = EQUIPMENT_LIST[lang]
    prod_html = ""
    test_html = ""
    for title, group, slug, bullets in items:
        items_html = "".join(f"<li>{it}</li>" for it in bullets)
        card = f'''<a class="app-card" href="equipment/{slug}.html">
        <div class="app-head"><h4>{title}</h4></div>
        <div class="app-body"><ul>{items_html}</ul>
          <div class="app-link">{d['equip_detail_link']}</div>
        </div>
      </a>'''
        if group == "production":
            prod_html += card
        else:
            test_html += card
    body = f"""
<section class="page-banner">
  <div class="container">
    <span class="eyebrow" style="color:#ffcf5c;">{d['equip_eyebrow']}</span>
    <h1>{d['equip_title']}</h1>
    <p>{d['equip_sub']}</p>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-title">{d['equip_group_production']}</h2>
    <div class="app-grid">
      {prod_html}
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <h2 class="section-title">{d['equip_group_testing']}</h2>
    <div class="app-grid">
      {test_html}
    </div>
  </div>
</section>
"""
    return page_shell(lang, "equipment", body)

def build_equipment_detail(lang, slug):
    d = C[lang]
    ed = EQUIPMENT_DETAIL[lang][slug]
    root_prefix = "../../"
    intro_html = "".join(f"<p>{p}</p>" for p in ed["intro"])
    hero_html = ""
    if ed.get("hero"):
        hero_html = f'''<div class="product-hero">
      <img src="{root_prefix}assets/equipment/{slug}/{ed['hero']}" alt="{ed['title']}">
    </div>'''
    specs_html = ""
    if ed.get("specs"):
        rows = "".join(f'<div class="info-row"><span class="k">{k}</span><span class="v">{v}</span></div>' for k,v in ed["specs"])
        specs_html = f'''<div class="info-card">
      <h4>{d['equip_specs_title']}</h4>
      {rows}
    </div>'''
    structure_html = "".join(f"<li>{it}</li>" for it in ed.get("structure", []))
    lang_target_path = {lg: f"equipment/{slug}.html" for lg in LANGS}
    body = f"""
<section class="page-banner">
  <div class="container">
    <span class="eyebrow" style="color:#ffcf5c;">{d['equip_doc_label']}: {ed['doc_code']}</span>
    <h1>{ed['title']}</h1>
    <p>{ed['subtitle']}</p>
  </div>
</section>

<section>
  <div class="container about-grid">
    <div>
      <a href="../equipment.html" class="back-link">{d['back_to_equipment']}</a>
      {hero_html}
      {intro_html}
      <h3 class="section-title" style="font-size:20px;">{d['equip_structure_title']}</h3>
      <ul class="app-body" style="padding:0;list-style:none;">{structure_html}</ul>
    </div>
    <div>
      {specs_html}
      <div class="qhse-card hse" style="margin-top:24px;">
        <h4>{d['equip_safety_title']}</h4>
        <p style="font-size:14.5px;color:var(--text);">{ed['safety']}</p>
      </div>
    </div>
  </div>
</section>
"""
    return page_shell(lang, "equipment", body, depth=1, lang_target_path=lang_target_path)

def build_product_detail(lang, slug):
    d = C[lang]
    pd = PRODUCT_DETAIL[lang][slug]
    root_prefix = "../../"
    intro_html = "".join(f"<p>{p}</p>" for p in pd["intro"])
    hero_html = ""
    if pd.get("hero"):
        hero_html = f'''<div class="product-hero">
      <img src="{root_prefix}assets/products/{slug}/{pd['hero']}" alt="{pd['title']}">
    </div>'''
    cards_html = ""
    for name, img, desc in pd["materials"]:
        if img:
            img_html = f'<img src="{root_prefix}assets/products/{slug}/{img}" alt="{name}">'
        else:
            img_html = '<div class="material-noimg">YMX</div>'
        cards_html += f'''<div class="material-card">
        <div class="material-img">{img_html}</div>
        <div class="material-body">
          <h4>{name}</h4>
          <p>{desc}</p>
        </div>
      </div>'''
    lang_target_path = {lg: f"products/{slug}.html" for lg in LANGS}
    body = f"""
<section class="page-banner">
  <div class="container">
    <span class="eyebrow" style="color:#ffcf5c;">{d['apps_eyebrow']}</span>
    <h1>{pd['title']}</h1>
    <p>{pd['subtitle']}</p>
  </div>
</section>

<section>
  <div class="container">
    <a href="../products.html" class="back-link">{d['back_to_products']}</a>
    {hero_html}
    {intro_html}
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <h2 class="section-title">{d['materials_title']}</h2>
    <div class="material-grid">
      {cards_html}
    </div>
  </div>
</section>
"""
    return page_shell(lang, "products", body, depth=1, lang_target_path=lang_target_path)

def build_quality(lang):
    d = C[lang]
    q_items = "".join(f"<li>{it}</li>" for it in d["quality_items"])
    h_items = "".join(f"<li>{it}</li>" for it in d["hse_items"])
    body = f"""
<section class="page-banner">
  <div class="container">
    <span class="eyebrow" style="color:#ffcf5c;">{d['qhse_eyebrow']}</span>
    <h1>{d['qhse_title']}</h1>
    <p>{d['qhse_sub']}</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="qhse-grid">
      <div class="qhse-card">
        <h4>{d['quality_title']}</h4>
        <ul>{q_items}</ul>
      </div>
      <div class="qhse-card hse">
        <h4>{d['hse_title']}</h4>
        <ul>{h_items}</ul>
      </div>
    </div>

    <div class="policy-box">
      <h4>{d['policy_title']}</h4>
      <p>{d['policy_text']}</p>
    </div>
  </div>
</section>
"""
    return page_shell(lang, "quality-hse", body)

def build_contact(lang):
    d = C[lang]
    items_html = ""
    for icon, label, val in d["contact_items"]:
        items_html += f'''<div class="contact-item">
          <div class="ic">{icon}</div>
          <div><b>{label}</b><span>{val}</span></div>
        </div>'''
    body = f"""
<section class="page-banner">
  <div class="container">
    <span class="eyebrow" style="color:#ffcf5c;">{d['contact_eyebrow']}</span>
    <h1>{d['contact_title']}</h1>
    <p>{d['contact_sub']}</p>
  </div>
</section>

<section>
  <div class="container contact-grid">
    <div class="contact-card">
      {items_html}
    </div>
    <div class="map-frame">
      <iframe loading="lazy" referrerpolicy="no-referrer-when-downgrade"
        src="https://www.google.com/maps?q=Khu+c%C3%B4ng+nghi%E1%BB%87p+Tam+Ph%C6%B0%E1%BB%9Bc%2C+%C4%90%E1%BB%93ng+Nai&output=embed">
      </iframe>
    </div>
  </div>
</section>
"""
    return page_shell(lang, "contact", body)

BUILDERS = {"index":build_index,"about":build_about,"products":build_products,"equipment":build_equipment,"quality-hse":build_quality,"contact":build_contact}

# ---- write files ----
os.makedirs(os.path.join(OUT,"assets"), exist_ok=True)
for lang in LANGS:
    os.makedirs(os.path.join(OUT,lang), exist_ok=True)
    os.makedirs(os.path.join(OUT,lang,"products"), exist_ok=True)
    os.makedirs(os.path.join(OUT,lang,"equipment"), exist_ok=True)
    for page_key, fname in PAGE_FILES.items():
        html = BUILDERS[page_key](lang)
        with open(os.path.join(OUT,lang,fname), "w", encoding="utf-8") as f:
            f.write(html)
    for slug in PRODUCT_DETAIL[lang].keys():
        html = build_product_detail(lang, slug)
        with open(os.path.join(OUT,lang,"products",f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(html)
    for slug in EQUIPMENT_DETAIL[lang].keys():
        html = build_equipment_detail(lang, slug)
        with open(os.path.join(OUT,lang,"equipment",f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(html)

# nav.js
with open(os.path.join(OUT,"assets","nav.js"), "w", encoding="utf-8") as f:
    f.write("""document.addEventListener('DOMContentLoaded',function(){
  var t=document.getElementById('navToggle'), m=document.getElementById('navMenu');
  if(t&&m){ t.addEventListener('click',function(){ m.classList.toggle('open'); });
    m.querySelectorAll('a').forEach(function(a){ a.addEventListener('click',function(){ m.classList.remove('open'); }); }); }
});""")

# copy CSS (only if a source stylesheet is provided next to this script / in /tmp build cache;
# otherwise the stylesheet already living in OUT/assets/style.css is left untouched)
import shutil
_css_candidates = [
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "style.css"),
    "/tmp/build/assets/style.css",
]
for _src in _css_candidates:
    if os.path.exists(_src):
        shutil.copyfile(_src, os.path.join(OUT,"assets","style.css"))
        break

# landing page (language selector) at OUT/index.html
landing_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>YMX Vietnam Electronic Technology | Select Language / Chọn ngôn ngữ / 选择语言</title>
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="assets/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<meta name="theme-color" content="#0b2a4a">
</head>
<body>
<div class="landing">
  <div class="landing-card">
    <img src="assets/logo.png" alt="YMX" class="landing-logo">
    <h1>YMX Vietnam Electronic Technology</h1>
    <p>Chọn ngôn ngữ &nbsp;/&nbsp; Select language &nbsp;/&nbsp; 选择语言</p>
    <div class="lang-options">
      <a class="lang-btn" href="vi/index.html"><b>Tiếng Việt</b><span>Trang tiếng Việt</span></a>
      <a class="lang-btn" href="en/index.html"><b>English</b><span>English site</span></a>
      <a class="lang-btn" href="zh/index.html"><b>中文</b><span>简体中文网站</span></a>
    </div>
  </div>
</div>
</body>
</html>
"""
with open(os.path.join(OUT,"index.html"), "w", encoding="utf-8") as f:
    f.write(landing_html)

print("DONE. Files written to", OUT)
