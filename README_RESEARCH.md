# مولد خطة البحث - Research Plan Generator

## 📋 نظرة عامة / Overview

أداة شاملة لإنشاء وإدارة خطط البحث الأكاديمية باللغتين العربية والإنجليزية. تساعد الباحثين والطلاب على تنظيم أبحاثهم بطريقة منهجية واحترافية.

A comprehensive tool for creating and managing academic research plans in both Arabic and English. Helps researchers and students organize their research systematically and professionally.

## ✨ المميزات / Features

### 🎯 المميزات الرئيسية / Main Features

- ✅ **قوالب شاملة**: قالب كامل لخطة البحث يغطي جميع الجوانب
- ✅ **ثنائي اللغة**: دعم كامل للعربية والإنجليزية
- ✅ **تفاعلي**: وضع تفاعلي لإنشاء الخطة خطوة بخطوة
- ✅ **تصدير متعدد**: حفظ بصيغة JSON و Markdown
- ✅ **إدارة كاملة**: إضافة وتعديل جميع عناصر الخطة
- ✅ **حسابات تلقائية**: حساب الميزانية والإحصائيات تلقائياً

### 📊 العناصر المدعومة / Supported Elements

1. **المعلومات الأساسية** / Basic Information
2. **الأهداف البحثية** / Research Objectives
3. **أسئلة البحث** / Research Questions
4. **الفرضيات** / Hypotheses
5. **الإطار النظري** / Theoretical Framework
6. **المنهجية** / Methodology
7. **الجدول الزمني** / Timeline
8. **الميزانية** / Budget
9. **المراجع** / References
10. **الاعتبارات الأخلاقية** / Ethical Considerations

## 🚀 البدء السريع / Quick Start

### المتطلبات / Requirements

- Python 3.7 أو أحدث / Python 3.7 or higher
- لا توجد مكتبات خارجية مطلوبة / No external libraries required

### التثبيت / Installation

```bash
# استنساخ المشروع أو تحميل الملفات
# Clone the project or download files

# لا حاجة لتثبيت مكتبات إضافية
# No need to install additional libraries
```

### الاستخدام / Usage

#### 1️⃣ الوضع التفاعلي / Interactive Mode

```bash
python research_plan_generator.py
```

اختر الخيار 1 لإنشاء خطة بحث تفاعلية:
- أدخل المعلومات الأساسية
- أضف الأهداف والأسئلة
- حدد المنهجية
- احفظ الخطة بصيغة JSON و Markdown

#### 2️⃣ إنشاء خطة نموذجية / Create Sample Plan

```bash
python research_plan_generator.py
```

اختر الخيار 2 لإنشاء خطة بحث نموذجية جاهزة.

#### 3️⃣ الاستخدام البرمجي / Programmatic Usage

```python
from research_plan_generator import ResearchPlan

# إنشاء خطة جديدة
plan = ResearchPlan()

# تعيين المعلومات الأساسية
plan.set_basic_info(
    title="عنوان البحث",
    researcher="اسم الباحث",
    institution="اسم المؤسسة"
)

# إضافة الأهداف
plan.add_objective("الهدف الأول")
plan.add_objective("الهدف الثاني")

# إضافة الأسئلة
plan.add_question("السؤال الأول؟")
plan.add_question("السؤال الثاني؟")

# إضافة فرضية
plan.add_hypothesis(
    null_hypothesis="الفرضية الصفرية",
    alternative_hypothesis="الفرضية البديلة"
)

# تعيين المنهجية
plan.set_methodology(
    research_type="بحث كمي",
    approach="منهج تجريبي",
    population="طلاب الجامعات",
    sample_size=300
)

# إضافة عنصر للجدول الزمني
plan.add_timeline_item(
    phase="1",
    activity="مراجعة الأدبيات",
    start_date="2025-01-01",
    end_date="2025-02-28"
)

# إضافة عنصر للميزانية
plan.add_budget_item(
    item="أدوات البحث",
    description="استبانات وبرامج",
    cost=5000.0
)

# إضافة مرجع
plan.add_reference(
    reference="المؤلف (2024). عنوان الكتاب. الناشر.",
    ref_type="arabic"
)

# حفظ الخطة
plan.save_to_json("my_research_plan.json")
plan.save_markdown("my_research_plan.md")

# طباعة ملخص
plan.print_summary()
```

## 📁 هيكل الملفات / File Structure

```
.
├── research_plan.md                    # قالب خطة البحث الشامل
├── research_plan_generator.py          # البرنامج الرئيسي
├── requirements_research.txt           # المتطلبات (اختياري)
├── README_RESEARCH.md                  # هذا الملف
└── [الملفات المولدة / Generated files]
    ├── research_plan.json              # خطة بصيغة JSON
    ├── research_plan_output.md         # خطة بصيغة Markdown
    └── sample_research_plan.*          # خطة نموذجية
```

## 🎓 أمثلة الاستخدام / Usage Examples

### مثال 1: بحث في التعليم / Education Research

```python
plan = ResearchPlan()
plan.set_basic_info(
    title="أثر التعلم الإلكتروني على التحصيل الدراسي",
    researcher="د. سارة أحمد",
    institution="جامعة الملك عبدالعزيز"
)

plan.add_objective("قياس أثر التعلم الإلكتروني على التحصيل")
plan.add_objective("تحديد التحديات في تطبيق التعلم الإلكتروني")

plan.add_question("ما مدى تأثير التعلم الإلكتروني على الطلاب؟")

plan.set_methodology(
    research_type="بحث كمي",
    approach="منهج شبه تجريبي",
    population="طلاب المرحلة الثانوية",
    sample_size=200
)

plan.save_to_json("education_research.json")
```

### مثال 2: بحث في علم النفس / Psychology Research

```python
plan = ResearchPlan()
plan.set_basic_info(
    title="العلاقة بين القلق والأداء الأكاديمي",
    researcher="د. محمد علي",
    institution="جامعة القاهرة"
)

plan.add_hypothesis(
    null_hypothesis="لا توجد علاقة بين القلق والأداء الأكاديمي",
    alternative_hypothesis="توجد علاقة سلبية بين القلق والأداء الأكاديمي"
)

plan.set_methodology(
    research_type="بحث ارتباطي",
    approach="منهج وصفي ارتباطي",
    population="طلاب الجامعات",
    sample_size=500
)

plan.save_markdown("psychology_research.md")
```

### مثال 3: بحث في الإدارة / Management Research

```python
plan = ResearchPlan()
plan.set_basic_info(
    title="تأثير القيادة التحويلية على الأداء المؤسسي",
    researcher="د. فاطمة حسن",
    institution="جامعة الإمارات"
)

plan.add_objective("تحليل أنماط القيادة التحويلية")
plan.add_objective("قياس تأثيرها على الأداء المؤسسي")
plan.add_objective("تطوير نموذج للقيادة الفعالة")

plan.add_budget_item("استبانات", "طباعة 1000 استبانة", 2000.0)
plan.add_budget_item("تحليل إحصائي", "SPSS وخدمات تحليل", 3000.0)
plan.add_budget_item("نشر", "رسوم نشر في مجلة محكمة", 5000.0)

total = plan.calculate_total_budget()
print(f"إجمالي الميزانية: {total} ريال")
```

## 📊 الوظائف الرئيسية / Main Functions

### فئة ResearchPlan / ResearchPlan Class

| الوظيفة / Function | الوصف / Description |
|-------------------|---------------------|
| `set_basic_info()` | تعيين المعلومات الأساسية / Set basic information |
| `add_objective()` | إضافة هدف بحثي / Add research objective |
| `add_question()` | إضافة سؤال بحثي / Add research question |
| `add_hypothesis()` | إضافة فرضية / Add hypothesis |
| `set_methodology()` | تعيين المنهجية / Set methodology |
| `add_timeline_item()` | إضافة عنصر للجدول الزمني / Add timeline item |
| `add_budget_item()` | إضافة عنصر للميزانية / Add budget item |
| `add_reference()` | إضافة مرجع / Add reference |
| `calculate_total_budget()` | حساب إجمالي الميزانية / Calculate total budget |
| `save_to_json()` | حفظ بصيغة JSON / Save as JSON |
| `load_from_json()` | تحميل من JSON / Load from JSON |
| `save_markdown()` | حفظ بصيغة Markdown / Save as Markdown |
| `print_summary()` | طباعة ملخص / Print summary |

## 🎨 التخصيص / Customization

### تخصيص القالب / Customize Template

يمكنك تعديل ملف `research_plan.md` لإضافة أو إزالة أقسام حسب احتياجاتك:

```markdown
## قسم جديد / New Section

### محتوى القسم / Section Content
[أضف المحتوى هنا]
```

### إضافة وظائف جديدة / Add New Functions

```python
class ResearchPlan:
    # ... الكود الموجود
    
    def add_limitation(self, limitation: str):
        """إضافة محدد بحثي"""
        if not hasattr(self, 'limitations'):
            self.limitations = []
        self.limitations.append(limitation)
    
    def add_expected_outcome(self, outcome: str):
        """إضافة نتيجة متوقعة"""
        if not hasattr(self, 'expected_outcomes'):
            self.expected_outcomes = []
        self.expected_outcomes.append(outcome)
```

## 📈 أمثلة متقدمة / Advanced Examples

### مثال: خطة بحث كاملة / Complete Research Plan

```python
from research_plan_generator import ResearchPlan

# إنشاء خطة شاملة
plan = ResearchPlan()

# 1. المعلومات الأساسية
plan.set_basic_info(
    title="تأثير الذكاء الاصطناعي على سوق العمل في المملكة العربية السعودية",
    researcher="د. عبدالله محمد الأحمد",
    institution="جامعة الملك سعود - كلية إدارة الأعمال"
)

# 2. الأهداف (5 أهداف)
objectives = [
    "تحليل التأثير الحالي للذكاء الاصطناعي على سوق العمل السعودي",
    "تحديد القطاعات الأكثر تأثراً بالذكاء الاصطناعي",
    "قياس مستوى الاستعداد للتحول الرقمي في المؤسسات",
    "تطوير إطار عمل لإدارة التغيير التكنولوجي",
    "تقديم توصيات لصناع القرار والمؤسسات"
]
for obj in objectives:
    plan.add_objective(obj)

# 3. الأسئلة (4 أسئلة)
questions = [
    "ما مدى تأثير الذكاء الاصطناعي على معدلات التوظيف في القطاعات المختلفة؟",
    "ما هي المهارات المطلوبة للتكيف مع التحول الرقمي؟",
    "كيف تستعد المؤسسات السعودية لدمج الذكاء الاصطناعي؟",
    "ما هي التحديات والفرص المرتبطة بهذا التحول؟"
]
for q in questions:
    plan.add_question(q)

# 4. الفرضيات (3 فرضيات)
hypotheses = [
    ("لا يوجد تأثير للذكاء الاصطناعي على معدلات التوظيف",
     "يوجد تأثير سلبي للذكاء الاصطناعي على معدلات التوظيف في بعض القطاعات"),
    
    ("لا توجد علاقة بين الاستعداد التكنولوجي وحجم المؤسسة",
     "توجد علاقة إيجابية بين الاستعداد التكنولوجي وحجم المؤسسة"),
    
    ("لا توجد فروق في التأثير بين القطاعات المختلفة",
     "توجد فروق دالة إحصائياً في التأثير بين القطاعات")
]
for null, alt in hypotheses:
    plan.add_hypothesis(null, alt)

# 5. المنهجية
plan.set_methodology(
    research_type="بحث مختلط (كمي ونوعي)",
    approach="منهج وصفي تحليلي",
    population="المؤسسات والشركات في المملكة العربية السعودية",
    sample_size=750
)

# 6. الجدول الزمني (8 مراحل)
timeline = [
    ("1", "مراجعة الأدبيات والدراسات السابقة", "2025-01-01", "2025-02-28"),
    ("2", "تطوير أدوات البحث (استبانة ومقابلات)", "2025-03-01", "2025-03-31"),
    ("3", "التحكيم والتعديل", "2025-04-01", "2025-04-15"),
    ("4", "جمع البيانات الكمية", "2025-04-16", "2025-06-30"),
    ("5", "إجراء المقابلات النوعية", "2025-05-01", "2025-06-30"),
    ("6", "تحليل البيانات", "2025-07-01", "2025-08-31"),
    ("7", "كتابة النتائج والتوصيات", "2025-09-01", "2025-10-31"),
    ("8", "المراجعة النهائية والتسليم", "2025-11-01", "2025-11-30")
]
for phase, activity, start, end in timeline:
    plan.add_timeline_item(phase, activity, start, end)

# 7. الميزانية (10 بنود)
budget_items = [
    ("أدوات البحث", "تصميم وطباعة 1000 استبانة", 5000.0),
    ("البرمجيات", "SPSS, NVivo, وأدوات تحليل", 8000.0),
    ("السفر والتنقل", "زيارات ميدانية لـ 50 مؤسسة", 15000.0),
    ("المقابلات", "تسجيل وتفريغ 30 مقابلة", 6000.0),
    ("التحكيم", "أتعاب 5 محكمين", 5000.0),
    ("الترجمة", "ترجمة الأدوات والنتائج", 4000.0),
    ("التدقيق اللغوي", "تدقيق عربي وإنجليزي", 3000.0),
    ("النشر", "رسوم نشر في مجلتين محكمتين", 10000.0),
    ("مساعد باحث", "راتب 6 أشهر", 24000.0),
    ("متفرقات", "نفقات غير متوقعة", 5000.0)
]
for item, desc, cost in budget_items:
    plan.add_budget_item(item, desc, cost)

# 8. المراجع (10 مراجع)
arabic_refs = [
    "العتيبي، خالد بن محمد (2023). الذكاء الاصطناعي وسوق العمل: دراسة تحليلية. الرياض: دار النشر العلمي.",
    "الغامدي، سارة أحمد (2024). التحول الرقمي في المؤسسات السعودية. مجلة الإدارة العامة، 64(2), 45-78.",
    "وزارة الموارد البشرية والتنمية الاجتماعية (2024). تقرير سوق العمل السعودي 2024. الرياض.",
    "الشمري، فهد عبدالله (2023). مستقبل الوظائف في عصر الذكاء الاصطناعي. جدة: دار الأندلس.",
    "هيئة الاتصالات وتقنية المعلومات (2024). مؤشر التحول الرقمي في المملكة. الرياض."
]

english_refs = [
    "Smith, J., & Johnson, M. (2024). Artificial Intelligence and Employment: A Global Perspective. Journal of Labor Economics, 42(3), 567-598.",
    "Brown, A. (2023). Digital Transformation in the Middle East. London: Oxford University Press.",
    "World Economic Forum (2024). The Future of Jobs Report 2024. Geneva: WEF Publications.",
    "Lee, K., & Chen, L. (2024). AI Adoption in Organizations: Challenges and Opportunities. MIT Sloan Management Review, 65(2), 23-45.",
    "McKinsey Global Institute (2024). AI and the Future of Work in Emerging Markets. New York: McKinsey & Company."
]

for ref in arabic_refs:
    plan.add_reference(ref, "arabic")
for ref in english_refs:
    plan.add_reference(ref, "english")

# 9. حفظ الخطة
plan.save_to_json("ai_labor_market_research.json")
plan.save_markdown("ai_labor_market_research.md")

# 10. طباعة الملخص
plan.print_summary()

# 11. عرض الميزانية
print(f"\n💰 إجمالي الميزانية: {plan.calculate_total_budget():,.2f} ريال سعودي")
```

## 🔧 استكشاف الأخطاء / Troubleshooting

### مشكلة: خطأ في الترميز / Encoding Error

```python
# الحل: تأكد من استخدام UTF-8
with open('file.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
```

### مشكلة: ملف غير موجود / File Not Found

```python
import os

# تحقق من وجود الملف قبل التحميل
if os.path.exists('research_plan.json'):
    plan.load_from_json('research_plan.json')
else:
    print("الملف غير موجود!")
```

## 📚 موارد إضافية / Additional Resources

### دلائل كتابة البحث / Research Writing Guides

- [دليل APA للتوثيق](https://apastyle.apa.org/)
- [دليل MLA للتوثيق](https://www.mla.org/)
- [دليل Chicago للتوثيق](https://www.chicagomanualofstyle.org/)

### أدوات مفيدة / Useful Tools

- **Zotero**: إدارة المراجع
- **Mendeley**: إدارة المراجع والتعاون
- **SPSS**: التحليل الإحصائي
- **NVivo**: تحليل البيانات النوعية
- **Grammarly**: التدقيق اللغوي

## 🤝 المساهمة / Contributing

نرحب بمساهماتكم! يمكنكم:

1. **الإبلاغ عن مشاكل** / Report issues
2. **اقتراح ميزات جديدة** / Suggest new features
3. **تحسين الكود** / Improve code
4. **إضافة أمثلة** / Add examples
5. **تحسين التوثيق** / Improve documentation

## 📄 الترخيص / License

هذا المشروع مفتوح المصدر ومتاح للاستخدام الأكاديمي والتعليمي.

This project is open source and available for academic and educational use.

## 📞 التواصل / Contact

للأسئلة والاستفسارات:
- البريد الإلكتروني / Email: [your-email@example.com]
- GitHub Issues: [رابط المشروع]

## 🙏 شكر وتقدير / Acknowledgments

شكراً لجميع الباحثين والأكاديميين الذين ساهموا في تطوير هذه الأداة.

Thanks to all researchers and academics who contributed to developing this tool.

---

**آخر تحديث / Last Updated:** 2025-11-14

**الإصدار / Version:** 1.0.0

---

## 📖 أمثلة إضافية / More Examples

### مثال: تحميل وتعديل خطة موجودة

```python
# تحميل خطة موجودة
plan = ResearchPlan()
plan.load_from_json("existing_plan.json")

# إضافة هدف جديد
plan.add_objective("هدف إضافي جديد")

# تعديل الميزانية
plan.add_budget_item("بند جديد", "وصف البند", 2000.0)

# حفظ التعديلات
plan.save_to_json("updated_plan.json")
plan.print_summary()
```

### مثال: إنشاء تقرير مخصص

```python
plan = ResearchPlan()
# ... إضافة البيانات

# توليد Markdown مخصص
md_content = plan.generate_markdown()

# إضافة محتوى إضافي
custom_content = """
## قسم إضافي مخصص

هذا محتوى إضافي خاص بمشروعي.
"""

full_content = md_content + custom_content

# حفظ
with open("custom_report.md", "w", encoding="utf-8") as f:
    f.write(full_content)
```

---

**استمتع باستخدام مولد خطة البحث! 🎓**

**Enjoy using the Research Plan Generator! 🎓**
