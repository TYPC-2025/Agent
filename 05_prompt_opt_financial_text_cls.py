import json
import random
import matplotlib.pyplot as plt

# ===================== 金融文本分类数据集 =====================
finance_dataset = [
    {"text": "央行发布降准公告，预计释放长期资金约1万亿元", "label": "新闻报道"},
    {"text": "本公司2025年一季度净利润同比增长25%，营收稳步提升", "label": "财务报道"},
    {"text": "公司召开股东大会，审议通过利润分配方案", "label": "公司公告"},
    {"text": "分析师给予某行业增持评级，看好长期成长空间", "label": "分析师报告"},
    {"text": "证监会加强信息披露监管，维护市场秩序", "label": "新闻报道"},
    {"text": "公司资产负债率下降，财务结构持续优化", "label": "财务报道"},
    {"text": "公司发布重大资产重组进展公告", "label": "公司公告"},
    {"text": "我们预计科技金融板块全年增速超20%", "label": "分析师报告"},
]

# ===================== 基础提示词（简陋版） =====================
base_prompt_messages = [
    {"role": "system", "content": "你是金融助手，把文本分类：新闻报道、财务报道、公司公告、分析师报告、不清楚类别"},
    {"role": "user", "content": "{text}"}
]

# ===================== 优化提示词（专业版） =====================
optimized_prompt_messages=[
    {"role": "system", "content": """你是专业金融文本分类器。
【分类规则】
1. 新闻报道：政策、市场、行业、监管动态
2. 财务报道：财报、利润、资产、负债、营收等财务数据
3. 公司公告：企业正式公告、会议、股权、重组等
4. 分析师报告：分析师观点、评级、预测、投资建议
5. 不清楚类别：无法判断

【输出要求】
- 只输出标签
- 不要多余文字
    """},
    {"role": "user", "content": "{text}"}
]

# ===================== 模拟模型分类函数 =====================
def simulate_model_classify(text, prompt_msgs):
    """模拟大模型根据提示词分类"""
    if "基础" in str(prompt_msgs):
        return random.choice(["新闻报道", "财务报道", "公司公告", "分析师报告", "不清楚类别"])

    # 优化提示词：规则匹配
    if any(i in text for i in ["央行", "证监会", "监管", "政策", "市场"]):
        return "新闻报道"
    elif any(i in text for i in ["净利润", "营收", "负债", "资产", "财报"]):
        return "财务报道"
    elif any(i in text for i in ["公告", "股东大会", "重组", "审议"]):
        return "公司公告"
    elif any(i in text for i in ["分析师", "评级", "预计", "看好"]):
        return "分析师报告"
    else:
        return "不清楚类别"

# ===================== 评估函数 =====================
def evaluate(dataset, prompt):
    correct = 0
    total = len(dataset)
    result = []

    for item in dataset:
        pred=simulate_model_classify(item["text"], prompt)
        result.append({"文本": item["text"], "真实标签": item["label"], "预测标签": pred})
        if pred == item["label"]:
            correct += 1
    return correct / total, result

# ===================== 主运行流程 =====================
if __name__ == "__main__":
    print("=" * 60)
    print(" 金融文本分类 - 提示词优化对比实验")
    print("=" * 60)

    acc_base, res_base = evaluate(finance_dataset, base_prompt_messages)
    acc_opt, res_opt = evaluate(finance_dataset, optimized_prompt_messages)

    print(f"\n基础提示词准确率：{acc_base:.2%}")
    print(f"优化提示词准确率：{acc_opt:.2%}")

    print("\n==== 优化后分类结果 ====")
    for r in res_opt:
        mark = "✅" if r["真实标签"] == r["预测标签"] else "❌"
        print(f"{mark} 真实：{r['真实标签']} | 预测：{r['预测标签']}")

    # 绘图
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.figure(figsize=(7, 5))
    plt.bar(["基础提示词", "优化提示词"], [acc_base, acc_opt], color=["#ff6f61", "#44d7b8"])
    plt.title("金融文本分类：提示词优化效果对比", fontsize=14)
    plt.ylabel("准确率")
    plt.ylim(0, 1.05)
    for i, v in enumerate([acc_base, acc_opt]):
        plt.text(i, v + 0.02, f"{v:.2%}", ha="center", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

    # 保存结果
    with open("classification_result.json", "w", encoding="utf-8") as f:
        json.dump({
            "base_accuracy": acc_base,
            "optimized_accuracy": acc_opt,
            "details": res_opt
        }, f, ensure_ascii=False, indent=2)

    print("\n✅ 实验完成！结果已保存到 classification_result.json")