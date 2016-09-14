$(function(){

    // 历年收案情况走势
    var documentDataYear = [513, 735, 449, 587, 753, 577, 711];

    // 新建图表
    var myChart = echarts.init(document.getElementById('chart'));

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption({
        color: ["#2983c3","#3786e5"],
        title : {
            text: '执行受案数量趋势图',
            textStyle: {
                fontSize: 20,
                color: "#195caa",
                fontWeight: "bold",
                textAlign: "center"
            }
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: '执行收案数量'
        },
        toolbox: {
            show: true,
            feature: {
                dataZoom: {},
                dataView: {readOnly: false},
                magicType: {type: ['line', 'bar']},
                restore: {},
                saveAsImage: {}
            }
        },
        xAxis:  {
            type: 'category',
            boundaryGap: false,
            data: ['2009','2010','2011','2012','2013','2014','2015'],
            axisTick: {
                show: false
            },
            axisLine: {
                show: false
            }
        },
        yAxis: {
            type: 'value',
            axisLabel: {
                formatter: '{value}'
            },
            axisTick: {
                show: false
            },
            axisLine: {
                show: false
            }
        },
        series: [
            {
                name:'执行收案数量',
                type:'line',
                data:documentDataYear,
                markPoint: {
                    data: [
                        {type: 'max', name: '最高收案数'},
                        {type: 'min', name: '最低收案数'}
                    ]
                },
                markLine: {
                    data: [
                        {type: 'average', name: '平均收案数'}
                    ]
                },
                areaStyle: {
                    normal: {
                        color: "#2983c3",
                        opacity: .2
                    }
                }
            }
        ]
    });

});