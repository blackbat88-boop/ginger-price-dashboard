// 手动录入的生姜价格数据
// 每天/每周从网站查看后更新此文件
// 数据来源网站：
//   - 惠农网：https://www.cnhnb.com/
//   - 一亩田：https://www.ymt.com/
//   - 农业农村部：http://pfsc.agri.cn/

const ManualPriceData = {
    // 最后更新时间
    lastUpdate: '2026-03-31 19:50',

    // 今日价格录入（从网站查看后填写）
    // 格式：产区名称 : 价格 (元/斤)
    todayPrices: {
        // 山东产区
        yishui_xiaojiang: 5.00,    // 沂水小黄姜
        anqiu_mianjiang: 4.20,     // 安丘面姜
        changyi_mianjiang: 4.00,   // 昌邑面姜
        laizhou_mianjiang: 3.80,   // 莱州面姜
        laiWu_mianjiang: 3.60,     // 莱芜面姜
        qingzhou_mianjiang: 3.50,  // 青州面姜
        rushan_nijiang: 3.30,      // 乳山泥姜

        // 河北产区
        fengrun_mianjiang: 3.80,   // 丰润面姜
        tangshan_mianjiang: 3.40,  // 唐山面姜

        // 云南产区
        luoping_xiaojiang: 5.50,   // 罗平小黄姜
        wenshan_xiaojiang: 5.20,   // 文山小黄姜

        // 其他产区
        leshan_dahuangjiang: 4.50, // 四川乐山大黄姜
    },

    // 全国均价（可以手动计算或估算）
    nationalAverage: 3.55,  // 元/斤

    // 沂水价格
    yishuiPrice: 4.25,  // 元/斤

    // 价格趋势（从网站查看后填写）
    // "上涨", "下跌", "稳定"
    trend: "稳定",

    // 备注/市场分析（可选）
    note: "产区购销一般，农户农忙种姜，卖货不积极。"
};
