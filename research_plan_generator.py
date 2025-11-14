#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مولد خطة البحث - Research Plan Generator
أداة لإنشاء وإدارة خطط البحث الأكاديمية

Author: Research Planning Tool
Date: 2025
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional


class ResearchPlan:
    """فئة لإدارة خطة البحث"""
    
    def __init__(self):
        self.title = ""
        self.researcher = ""
        self.institution = ""
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.objectives = []
        self.questions = []
        self.hypotheses = []
        self.methodology = {}
        self.timeline = []
        self.budget = []
        self.references = []
        
    def set_basic_info(self, title: str, researcher: str, institution: str):
        """تعيين المعلومات الأساسية"""
        self.title = title
        self.researcher = researcher
        self.institution = institution
        
    def add_objective(self, objective: str):
        """إضافة هدف بحثي"""
        self.objectives.append(objective)
        
    def add_question(self, question: str):
        """إضافة سؤال بحثي"""
        self.questions.append(question)
        
    def add_hypothesis(self, null_hypothesis: str, alternative_hypothesis: str):
        """إضافة فرضية"""
        self.hypotheses.append({
            "null": null_hypothesis,
            "alternative": alternative_hypothesis
        })
        
    def set_methodology(self, research_type: str, approach: str, 
                       population: str, sample_size: int):
        """تعيين المنهجية"""
        self.methodology = {
            "type": research_type,
            "approach": approach,
            "population": population,
            "sample_size": sample_size
        }
        
    def add_timeline_item(self, phase: str, activity: str, 
                         start_date: str, end_date: str):
        """إضافة عنصر للجدول الزمني"""
        self.timeline.append({
            "phase": phase,
            "activity": activity,
            "start_date": start_date,
            "end_date": end_date
        })
        
    def add_budget_item(self, item: str, description: str, cost: float):
        """إضافة عنصر للميزانية"""
        self.budget.append({
            "item": item,
            "description": description,
            "cost": cost
        })
        
    def add_reference(self, reference: str, ref_type: str = "arabic"):
        """إضافة مرجع"""
        self.references.append({
            "reference": reference,
            "type": ref_type
        })
        
    def calculate_total_budget(self) -> float:
        """حساب إجمالي الميزانية"""
        return sum(item["cost"] for item in self.budget)
    
    def to_dict(self) -> Dict:
        """تحويل الخطة إلى قاموس"""
        return {
            "basic_info": {
                "title": self.title,
                "researcher": self.researcher,
                "institution": self.institution,
                "date": self.date
            },
            "objectives": self.objectives,
            "questions": self.questions,
            "hypotheses": self.hypotheses,
            "methodology": self.methodology,
            "timeline": self.timeline,
            "budget": {
                "items": self.budget,
                "total": self.calculate_total_budget()
            },
            "references": self.references
        }
    
    def save_to_json(self, filename: str = "research_plan.json"):
        """حفظ الخطة في ملف JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
        print(f"✓ تم حفظ الخطة في: {filename}")
        
    def load_from_json(self, filename: str):
        """تحميل الخطة من ملف JSON"""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        self.title = data["basic_info"]["title"]
        self.researcher = data["basic_info"]["researcher"]
        self.institution = data["basic_info"]["institution"]
        self.date = data["basic_info"]["date"]
        self.objectives = data["objectives"]
        self.questions = data["questions"]
        self.hypotheses = data["hypotheses"]
        self.methodology = data["methodology"]
        self.timeline = data["timeline"]
        self.budget = data["budget"]["items"]
        self.references = data["references"]
        
        print(f"✓ تم تحميل الخطة من: {filename}")
        
    def generate_markdown(self) -> str:
        """توليد خطة البحث بصيغة Markdown"""
        md = f"""# خطة البحث - {self.title}

## المعلومات الأساسية

- **الباحث:** {self.researcher}
- **المؤسسة:** {self.institution}
- **التاريخ:** {self.date}

---

## الأهداف البحثية

"""
        for i, obj in enumerate(self.objectives, 1):
            md += f"{i}. {obj}\n"
            
        md += "\n---\n\n## أسئلة البحث\n\n"
        for i, q in enumerate(self.questions, 1):
            md += f"{i}. {q}\n"
            
        md += "\n---\n\n## الفرضيات\n\n"
        for i, h in enumerate(self.hypotheses, 1):
            md += f"### الفرضية {i}\n"
            md += f"- **H₀:** {h['null']}\n"
            md += f"- **H₁:** {h['alternative']}\n\n"
            
        md += "---\n\n## المنهجية\n\n"
        md += f"- **نوع البحث:** {self.methodology.get('type', 'غير محدد')}\n"
        md += f"- **المنهج:** {self.methodology.get('approach', 'غير محدد')}\n"
        md += f"- **المجتمع:** {self.methodology.get('population', 'غير محدد')}\n"
        md += f"- **حجم العينة:** {self.methodology.get('sample_size', 0)}\n"
        
        md += "\n---\n\n## الجدول الزمني\n\n"
        md += "| المرحلة | النشاط | تاريخ البدء | تاريخ الانتهاء |\n"
        md += "|---------|--------|------------|----------------|\n"
        for item in self.timeline:
            md += f"| {item['phase']} | {item['activity']} | {item['start_date']} | {item['end_date']} |\n"
            
        md += "\n---\n\n## الميزانية\n\n"
        md += "| البند | الوصف | التكلفة |\n"
        md += "|-------|-------|--------|\n"
        for item in self.budget:
            md += f"| {item['item']} | {item['description']} | {item['cost']:.2f} |\n"
        md += f"| **المجموع** | | **{self.calculate_total_budget():.2f}** |\n"
        
        md += "\n---\n\n## المراجع\n\n"
        arabic_refs = [r for r in self.references if r['type'] == 'arabic']
        english_refs = [r for r in self.references if r['type'] == 'english']
        
        if arabic_refs:
            md += "### مراجع عربية\n\n"
            for i, ref in enumerate(arabic_refs, 1):
                md += f"{i}. {ref['reference']}\n"
                
        if english_refs:
            md += "\n### مراجع أجنبية\n\n"
            for i, ref in enumerate(english_refs, 1):
                md += f"{i}. {ref['reference']}\n"
        
        return md
    
    def save_markdown(self, filename: str = "research_plan_output.md"):
        """حفظ الخطة بصيغة Markdown"""
        md_content = self.generate_markdown()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"✓ تم حفظ الخطة بصيغة Markdown في: {filename}")
        
    def print_summary(self):
        """طباعة ملخص الخطة"""
        print("\n" + "="*60)
        print(f"📋 ملخص خطة البحث: {self.title}")
        print("="*60)
        print(f"👤 الباحث: {self.researcher}")
        print(f"🏛️  المؤسسة: {self.institution}")
        print(f"📅 التاريخ: {self.date}")
        print(f"\n🎯 عدد الأهداف: {len(self.objectives)}")
        print(f"❓ عدد الأسئلة: {len(self.questions)}")
        print(f"🔬 عدد الفرضيات: {len(self.hypotheses)}")
        print(f"📊 عدد مراحل الجدول الزمني: {len(self.timeline)}")
        print(f"💰 إجمالي الميزانية: {self.calculate_total_budget():.2f}")
        print(f"📚 عدد المراجع: {len(self.references)}")
        print("="*60 + "\n")


def create_sample_plan() -> ResearchPlan:
    """إنشاء خطة بحث نموذجية"""
    plan = ResearchPlan()
    
    # المعلومات الأساسية
    plan.set_basic_info(
        title="تأثير الذكاء الاصطناعي على التعليم العالي",
        researcher="د. أحمد محمد",
        institution="جامعة الملك سعود"
    )
    
    # الأهداف
    plan.add_objective("دراسة تأثير الذكاء الاصطناعي على جودة التعليم")
    plan.add_objective("تحليل تحديات تطبيق الذكاء الاصطناعي في الجامعات")
    plan.add_objective("تطوير إطار عمل لدمج الذكاء الاصطناعي في المناهج")
    
    # الأسئلة
    plan.add_question("ما مدى تأثير الذكاء الاصطناعي على نتائج الطلاب؟")
    plan.add_question("ما هي التحديات الرئيسية في تطبيق الذكاء الاصطناعي؟")
    plan.add_question("كيف يمكن تحسين استخدام الذكاء الاصطناعي في التعليم؟")
    
    # الفرضيات
    plan.add_hypothesis(
        "لا يوجد تأثير للذكاء الاصطناعي على أداء الطلاب",
        "يوجد تأثير إيجابي للذكاء الاصطناعي على أداء الطلاب"
    )
    
    # المنهجية
    plan.set_methodology(
        research_type="بحث مختلط (كمي ونوعي)",
        approach="منهج تجريبي",
        population="طلاب الجامعات السعودية",
        sample_size=500
    )
    
    # الجدول الزمني
    plan.add_timeline_item("1", "مراجعة الأدبيات", "2025-01-01", "2025-02-28")
    plan.add_timeline_item("2", "تطوير الأدوات", "2025-03-01", "2025-04-30")
    plan.add_timeline_item("3", "جمع البيانات", "2025-05-01", "2025-07-31")
    plan.add_timeline_item("4", "تحليل البيانات", "2025-08-01", "2025-09-30")
    plan.add_timeline_item("5", "كتابة النتائج", "2025-10-01", "2025-11-30")
    
    # الميزانية
    plan.add_budget_item("أدوات البحث", "استبانات وبرامج", 5000.0)
    plan.add_budget_item("السفر", "زيارات ميدانية", 3000.0)
    plan.add_budget_item("البرمجيات", "SPSS وأدوات تحليل", 2000.0)
    plan.add_budget_item("النشر", "رسوم النشر", 4000.0)
    
    # المراجع
    plan.add_reference(
        "العتيبي، خالد (2023). الذكاء الاصطناعي في التعليم. الرياض: دار النشر العلمي.",
        "arabic"
    )
    plan.add_reference(
        "Smith, J. (2024). AI in Higher Education. Journal of Educational Technology, 15(2), 45-67.",
        "english"
    )
    
    return plan


def interactive_mode():
    """وضع تفاعلي لإنشاء خطة بحث"""
    print("\n" + "="*60)
    print("🎓 مرحباً بك في مولد خطة البحث")
    print("="*60 + "\n")
    
    plan = ResearchPlan()
    
    # المعلومات الأساسية
    print("📝 المعلومات الأساسية:")
    title = input("عنوان البحث: ")
    researcher = input("اسم الباحث: ")
    institution = input("المؤسسة: ")
    plan.set_basic_info(title, researcher, institution)
    
    # الأهداف
    print("\n🎯 الأهداف البحثية:")
    print("(اضغط Enter بدون إدخال للانتقال للقسم التالي)")
    while True:
        obj = input(f"الهدف {len(plan.objectives) + 1}: ")
        if not obj:
            break
        plan.add_objective(obj)
    
    # الأسئلة
    print("\n❓ أسئلة البحث:")
    while True:
        q = input(f"السؤال {len(plan.questions) + 1}: ")
        if not q:
            break
        plan.add_question(q)
    
    # المنهجية
    print("\n🔬 المنهجية:")
    research_type = input("نوع البحث (كمي/نوعي/مختلط): ")
    approach = input("المنهج (تجريبي/وصفي/تحليلي): ")
    population = input("مجتمع البحث: ")
    sample_size = int(input("حجم العينة: ") or "0")
    plan.set_methodology(research_type, approach, population, sample_size)
    
    # حفظ الخطة
    print("\n💾 حفظ الخطة:")
    save_choice = input("هل تريد حفظ الخطة؟ (نعم/لا): ").lower()
    if save_choice in ['نعم', 'yes', 'y']:
        json_file = input("اسم ملف JSON (اضغط Enter للافتراضي): ") or "research_plan.json"
        md_file = input("اسم ملف Markdown (اضغط Enter للافتراضي): ") or "research_plan_output.md"
        
        plan.save_to_json(json_file)
        plan.save_markdown(md_file)
    
    plan.print_summary()
    
    return plan


def main():
    """الدالة الرئيسية"""
    print("\n" + "="*60)
    print("🎓 مولد خطة البحث - Research Plan Generator")
    print("="*60)
    print("\nاختر أحد الخيارات:")
    print("1. إنشاء خطة بحث تفاعلية")
    print("2. إنشاء خطة بحث نموذجية")
    print("3. تحميل خطة بحث موجودة")
    print("4. الخروج")
    
    choice = input("\nاختيارك (1-4): ")
    
    if choice == "1":
        plan = interactive_mode()
    elif choice == "2":
        print("\n📋 إنشاء خطة بحث نموذجية...")
        plan = create_sample_plan()
        plan.save_to_json("sample_research_plan.json")
        plan.save_markdown("sample_research_plan.md")
        plan.print_summary()
    elif choice == "3":
        filename = input("اسم ملف JSON: ")
        if os.path.exists(filename):
            plan = ResearchPlan()
            plan.load_from_json(filename)
            plan.print_summary()
        else:
            print(f"❌ الملف {filename} غير موجود!")
    elif choice == "4":
        print("\n👋 شكراً لاستخدامك مولد خطة البحث!")
        return
    else:
        print("❌ اختيار غير صحيح!")


if __name__ == "__main__":
    main()
