import os
import re

DATA = {
    "vi": {
        "index.html": ("Trang chủ - YMX Việt Nam | Chuyên gia cắt bế chính xác linh kiện điện tử", "Trang chủ Công ty TNHH Electronic Technology YMX Việt Nam - chuyên sản xuất, gia công cắt bế chính xác vật liệu điện tử phục vụ điện thoại, máy tính, ô tô."),
        "about.html": ("Giới thiệu công ty - YMX Việt Nam | Thông tin pháp lý & năng lực hoạt động", "Thông tin pháp lý, năng lực hoạt động và quá trình phát triển của Công ty TNHH Electronic Technology YMX Việt Nam tại KCN Tam Phước, Đồng Nai."),
        "products.html": ("Sản phẩm & Ứng dụng - YMX Việt Nam | Giải pháp cắt bế chính xác", "Năng lực cạnh tranh cốt lõi và các lĩnh vực ứng dụng sản phẩm cắt bế chính xác: điện thoại, laptop, ô tô, đèn nền, máy in."),
        "equipment.html": ("Thiết bị sản xuất & Kiểm tra - YMX Việt Nam | Máy cắt bế, cán màng, đo lường", "Hệ thống máy xẻ rãnh, cắt cuộn, cắt khuôn, cán màng và thiết bị đo lường VMM, thử lực kéo tại nhà máy YMX Việt Nam."),
        "quality-hse.html": ("Chất lượng & HSE - YMX Việt Nam | An toàn - Sức khỏe - Môi trường", "Cam kết quản lý chất lượng IQC/IPQC/OQC và chính sách An toàn - Sức khỏe - Môi trường (HSE) tại nhà máy YMX Việt Nam."),
        "contact.html": ("Liên hệ - YMX Việt Nam | Địa chỉ nhà máy & Thông tin liên lạc", "Liên hệ Công ty TNHH Electronic Technology YMX Việt Nam - Nhà xưởng 3A, Lô 33, KCN Tam Phước, Đồng Nai. Email: steven@ljdzsz.com"),
        "products/printer.html": ("Máy in / Photocopy - Sản phẩm cắt bế YMX Việt Nam", "Sản phẩm cắt bế chính xác cho máy in, photocopy: đệm chống tĩnh điện, vật liệu dẫn điện, chống nhiễu, thấm hút mực."),
        "products/mobile.html": ("Điện thoại di động - Sản phẩm cắt bế YMX Việt Nam", "Sản phẩm cắt bế cho điện thoại: băng keo 2 mặt, tấm tản nhiệt graphite, màng bảo vệ, Poron, Kapton, chống nhiễu EMI."),
        "products/notebook.html": ("Máy tính xách tay - Sản phẩm cắt bế YMX Việt Nam", "Sản phẩm cắt bế cho laptop: tấm PC/PP/PET, bọt dẫn điện, tấm dẫn nhiệt CPU, tem nhãn, đồng/nhôm lá."),
        "products/backlight.html": ("Module đèn nền (Backlight) - Sản phẩm cắt bế YMX Việt Nam", "Sản phẩm cắt bế cho module đèn nền: băng che sáng, tấm phản xạ, tấm khuếch tán, màng tăng sáng, mút đệm."),
        "products/automobile.html": ("Ô tô / Pin - Sản phẩm cắt bế YMX Việt Nam", "Sản phẩm cắt bế cho ô tô và pin: nỉ nội thất, băng keo 2 mặt, bông hút âm, mút giảm ồn, băng cách điện."),
        "products/other.html": ("Ứng dụng khác - Sản phẩm cắt bế YMX Việt Nam", "Ứng dụng cắt bế đa dạng: tủ điện, tem năng lượng, băng viền pin mặt trời, vòng đệm silicone, băng chịu nhiệt."),
        "equipment/xe-ranh.html": ("Máy xẻ rãnh - Thiết bị sản xuất YMX Việt Nam", "Máy xẻ rãnh tại nhà máy YMX Việt Nam: xẻ chia cuộn vật liệu, mắt điện chỉnh biên, tốc độ 3-10 m/phút, khổ liệu tối đa 1.300mm."),
        "equipment/cat-cuon.html": ("Máy cắt cuộn (Slitting) - Thiết bị sản xuất YMX Việt Nam", "Máy cắt cuộn FCA-1600 tại YMX Việt Nam: dao tròn, công suất 7.5kW, điện áp 380V, điều khiển HMI."),
        "equipment/cat-khuon.html": ("Máy cắt khuôn (Die-Cutting) - Thiết bị sản xuất YMX Việt Nam", "Máy cắt khuôn tại YMX Việt Nam: độ chính xác ±0.1mm, tốc độ 10-80 m/phút, servo motor, PLC+HMI lưu công thức."),
        "equipment/can-mang.html": ("Máy cán màng, dán màng - Thiết bị sản xuất YMX Việt Nam", "Máy cán màng dán màng tại YMX Việt Nam: lô cán silicone, bàn hút chân không, giá cuộn cấp và thu màng phế riêng biệt."),
        "equipment/can-mang-new.html": ("Máy cán màng Model mới - Thiết bị sản xuất YMX Việt Nam", "Máy cán màng model mới tại YMX Việt Nam: tích hợp cụm ép-cán nhiệt, dao cắt trên dây chuyền, HMI & PLC, cảm biến lực căng."),
        "equipment/vmm.html": ("Máy đo VMM (2D) - Thiết bị kiểm tra YMX Việt Nam", "Máy đo tọa độ hình ảnh VMM 2D tại YMX Việt Nam: đo điểm, đường, tròn, khoảng cách, hiệu chuẩn ba vòng tròn chuẩn."),
        "equipment/luc-keo.html": ("Máy thử lực kéo - Thiết bị kiểm tra YMX Việt Nam", "Máy thử lực kéo, độ bám dính tại YMX Việt Nam: thử kéo, nén, uốn, cắt, xé, bóc tách, phần mềm TM2101.")
    },
    "en": {
        "index.html": ("Home - YMX Vietnam | Precision Die-Cutting for Electronics", "YMX Vietnam Electronic Technology - precision die-cutting manufacturer for mobile phones, laptops, automobiles and electronic devices worldwide."),
        "about.html": ("About Us - YMX Vietnam | Company Profile & Legal Information", "Company profile, legal information and development history of YMX Vietnam Electronic Technology at Tam Phuoc Industrial Zone, Dong Nai Province."),
        "products.html": ("Products & Applications - YMX Vietnam | Die-Cutting Solutions", "Core competencies and application areas: precision die-cut components for printers, mobile phones, laptops, backlight modules, automobiles."),
        "equipment.html": ("Production & Testing Equipment - YMX Vietnam | Manufacturing Capabilities", "Slitting, roll cutting, die-cutting, laminating machines and VMM, tensile testing equipment at YMX Vietnam factory."),
        "quality-hse.html": ("Quality & HSE - YMX Vietnam | Health, Safety & Environment Policy", "Quality management system IQC/IPQC/OQC and Health-Safety-Environment (HSE) commitment at YMX Vietnam factory."),
        "contact.html": ("Contact Us - YMX Vietnam | Factory Address & Business Info", "Contact YMX Vietnam Electronic Technology - Workshop 3A, Lot 33, Tam Phuoc Industrial Zone, Dong Nai. Email: steven@ljdzsz.com"),
        "products/printer.html": ("Printer / Copier Components - YMX Vietnam Products", "Precision die-cut components for printers and copiers: anti-static pads, conductive products, shielding, ink-absorbing materials."),
        "products/mobile.html": ("Mobile Phone Components - YMX Vietnam Products", "Die-cut components for mobile phones: double-sided tape, graphite heat dissipation, dust-proof mesh, protective film, Poron, Kapton."),
        "products/notebook.html": ("Laptop / Notebook Components - YMX Vietnam Products", "Die-cut components for laptops: PC/PP/PET sheets, conductive foam, thermal pads for CPU, labels, copper/aluminum foil."),
        "products/backlight.html": ("Backlight Module Components - YMX Vietnam Products", "Die-cut components for backlight modules: light blocking tape, reflective sheets, diffusion sheets, brightness enhancement film."),
        "products/automobile.html": ("Automobile / Battery Components - YMX Vietnam Products", "Die-cut components for automobiles and batteries: felt, double-sided tape, sound-absorbing cotton, sponge, insulation tape."),
        "products/other.html": ("Other Applications - YMX Vietnam Products", "Diverse die-cutting applications: electrical cabinets, energy labels, solar panel edge tape, silicone rings, high-temperature tape."),
        "equipment/xe-ranh.html": ("Slitting Machine - YMX Vietnam Production Equipment", "Slitting machine at YMX Vietnam: splits material rolls, edge alignment sensor, speed 3-10 m/min, max width 1,300mm."),
        "equipment/cat-cuon.html": ("Roll Cutting Machine - YMX Vietnam Production Equipment", "FCA-1600 roll cutting machine at YMX Vietnam: rotary blade cutting, 7.5kW power, 380V, HMI control system."),
        "equipment/cat-khuon.html": ("Die-Cutting Machine - YMX Vietnam Production Equipment", "Die-cutting machine at YMX Vietnam: ±0.1mm precision, 10-80 m/min speed, servo motor drive, PLC+HMI recipe storage."),
        "equipment/can-mang.html": ("Laminating Machine - YMX Vietnam Production Equipment", "Laminating machine at YMX Vietnam: silicone rollers, vacuum table, separate film supply and waste collection."),
        "equipment/can-mang-new.html": ("Laminating Machine (New Model) - YMX Vietnam Production Equipment", "New model laminating machine at YMX Vietnam: integrated heat press, inline cutting, HMI & PLC control, tension sensor."),
        "equipment/vmm.html": ("VMM 2D Measuring Machine - YMX Vietnam Testing Equipment", "VMM 2D image measuring machine at YMX Vietnam: measures points, lines, circles, distances. Three-circle calibration method."),
        "equipment/luc-keo.html": ("Tensile Testing Machine - YMX Vietnam Testing Equipment", "Tensile and adhesion testing machine at YMX Vietnam: pull, compress, bend, cut, tear, peel tests with TM2101 software.")
    },
    "zh": {
        "index.html": ("首页 - 越南YMX电子科技 | 精密模切电子元器件制造专家", "越南YMX电子科技有限公司首页 - 专注手机、笔记本、汽车等电子元器件精密模切生产与加工。"),
        "about.html": ("公司简介 - 越南YMX电子科技 | 企业信息与发展历程", "越南YMX电子科技有限公司简介：法律信息、发展历程、全球工厂网络，位于同奈省新福工业区。"),
        "products.html": ("产品与应用 - 越南YMX电子科技 | 精密模切解决方案", "核心竞争力与产品应用领域：打印机、手机、笔记本、背光模组、汽车精密模切组件。"),
        "equipment.html": ("生产与检测设备 - 越南YMX电子科技 | 制造能力", "越南YMX工厂设备：开槽机、卷材切割机、模切机、覆膜机及VMM测量仪、拉力试验机。"),
        "quality-hse.html": ("质量与HSE - 越南YMX电子科技 | 安全健康环保", "越南YMX电子科技质量管理体系IQC/IPQC/OQC及健康安全环保(HSE)承诺。"),
        "contact.html": ("联系我们 - 越南YMX电子科技 | 工厂地址与联系方式", "联系越南YMX电子科技有限公司 - 3A车间，33号地块，新福工业区，同奈省。邮箱：steven@ljdzsz.com"),
        "products/printer.html": ("打印机/复印机组件 - 越南YMX电子科技产品", "打印机复印机精密模切组件：防静电垫、导电产品、屏蔽材料、吸墨棉。"),
        "products/mobile.html": ("手机组件 - 越南YMX电子科技产品", "手机精密模切组件：双面胶、石墨散热片、防尘网、保护膜、Poron、Kapton。"),
        "products/notebook.html": ("笔记本电脑组件 - 越南YMX电子科技产品", "笔记本精密模切组件：PC/PP/PET片材、导电泡棉、CPU导热片、标签、铜/铝箔。"),
        "products/backlight.html": ("背光模组组件 - 越南YMX电子科技产品", "背光模组精密模切组件：遮光胶带、反射片、扩散片、增亮膜、保护膜、缓冲泡棉。"),
        "products/automobile.html": ("汽车/电池组件 - 越南YMX电子科技产品", "汽车及电池精密模切组件：毛毡、双面胶、吸音棉、海绵、麦拉纸、绝缘胶带。"),
        "products/other.html": ("其他应用 - 越南YMX电子科技产品", "多元模切应用：电气柜、能效标签、太阳能板边框胶带、硅胶密封圈、耐高温胶带。"),
        "equipment/xe-ranh.html": ("开槽机 - 越南YMX电子科技生产设备", "越南YMX工厂开槽机：分切卷材，光电纠偏，速度3-10米/分钟，最大幅宽1300mm。"),
        "equipment/cat-cuon.html": ("卷材切割机 - 越南YMX电子科技生产设备", "越南YMX工厂FCA-1600卷材切割机：圆刀切割，功率7.5kW，电压380V，HMI控制。"),
        "equipment/cat-khuon.html": ("模切机 - 越南YMX电子科技生产设备", "越南YMX工厂模切机：精度±0.1mm，速度10-80米/分钟，伺服电机驱动，PLC+HMI配方存储。"),
        "equipment/can-mang.html": ("覆膜机 - 越南YMX电子科技生产设备", "越南YMX工厂覆膜机：硅胶辊压合，真空吸附工作台，独立供膜和废膜收卷。"),
        "equipment/can-mang-new.html": ("覆膜机（新款）- 越南YMX电子科技生产设备", "越南YMX工厂新款覆膜机：集成热压组件，在线切割，HMI及PLC控制，张力传感器。"),
        "equipment/vmm.html": ("VMM二维测量仪 - 越南YMX电子科技检测设备", "越南YMX工厂VMM二维影像测量仪：测量点、线、圆、距离，三圆校准法。"),
        "equipment/luc-keo.html": ("拉力试验机 - 越南YMX电子科技检测设备", "越南YMX工厂拉力及粘附力试验机：拉伸、压缩、弯曲、切割、撕裂、剥离测试，TM2101软件。")
    }
}

base_dir = r"e:\YMX Websile"

def process():
    for lang, pages in DATA.items():
        for page, (title, desc) in pages.items():
            filepath = os.path.join(base_dir, lang, page.replace('/', os.sep))
            if not os.path.exists(filepath):
                print(f"Not found: {filepath}")
                continue
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace title
            content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)
            
            # Replace description
            content = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', content)
            
            # Add favicon
            depth = page.count('/')
            favicon_path = "../" * (depth + 1) + "assets/favicon.svg"
            favicon_tag = f'<link rel="icon" type="image/svg+xml" href="{favicon_path}">'
            
            # If favicon already exists, replace it, else add it after stylesheet
            if 'rel="icon"' in content:
                content = re.sub(r'<link rel="icon".*?>', favicon_tag, content)
            else:
                content = re.sub(r'(<link rel="stylesheet".*?>)', r'\1\n' + favicon_tag, content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filepath}")

process()
