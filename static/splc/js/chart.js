$(function(){

    // 2015全院收案情况
    var acceptance = [2194, 1218, 294, 4058, 595, 520, 2771,1412];
    // 2015全院结案情况
    var lawsuit = [2141, 1683, 212, 4160, 573, 507, 2481,1252];
    // 历年收案情况走势
    var documentDataYear = [2065,5433,12463,13823,17912,18694,5333];
    // 各类案件受理总数
    var caseCourt = [45623,23080,8338,6809,12827,1548,1054,758];

    // 新建图表
    var myChart = echarts.init(document.getElementById('chart1'));
    var myChart1 = echarts.init(document.getElementById('chart2'));
    var myChart2 = echarts.init(document.getElementById('chart3'));

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption({
        color: ["#f1ad38","#3786e5"],
        title : {
            text: '全院收案和结案情况表',
            textStyle: {
                fontSize: 20,
                color: "#195caa",
                fontWeight: "bold",
                textAlign: "center"
            }
        },
        tooltip : {
            trigger: 'axis'
        },
        legend: {
            data:['收案情况','结案情况']
        },
        toolbox: {
            show : true,
            feature : {
                dataView : {show: true, readOnly: false},
                magicType : {show: true, type: ['line', 'bar']},
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        calculable : true,
        xAxis : [
            {
                type : 'category',
                data : ['第一法庭','第二法庭','第三法庭','第四法庭','第五法庭','第六法庭','第七法庭','第十一法庭'],
                axisTick: {
                    show: false
                },
                splitLine: {
                    show: false
                }
            }
        ],
        yAxis : [
            {
                type : 'value',
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                }
            }
        ],
        series : [
            {
                name:'收案情况',
                type:'bar',
                data:acceptance,
                markPoint : {
                    data : [
                        {type : 'max', name: '最大值'},
                        {type : 'min', name: '最小值'}
                    ]
                },
                barWidth: 30
            },
            {
                name:'结案情况',
                type:'bar',
                data:lawsuit,
                markPoint : {
                    data : [
                        {type : 'max', name: '最大值'},
                        {type : 'min', name: '最小值'}
                    ]
                },
                barWidth: 30
            }
        ]
    });

    myChart1.setOption({
        color: ["#f1ad38"],
        title: {
            text: '收案情况趋势表',
            textStyle: {
                fontWeight: "bold",
                textAlign: "center",
                fontSize: 16
            },
            x: 'left',
            y: 10
        },
        tooltip: {
            trigger: 'axis'
        },
        xAxis: {
            data: ["2010","2011","2012","2013","2014","2015","2016",],
            axisTick: {
                show: false
            },
            type: 'category',
            boundaryGap: false,
        },
        yAxis: {
            type: 'value',
            axisTick: {
                show: false
            }
        },
        series: [{
            type: 'line',
            name: "文书数量",
            smooth: true,
            data: documentDataYear,
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'}
                ]
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ]
            },
            areaStyle: {
                normal: {
                    color: "#f1ad38",
                    opacity: .3
                }
            }
        }]
    });

     myChart2.setOption({
        x:'top',
        color: ["#f1ad38","#ea6103","#fbad03","#ffff20","#2599dc","#ffde5a","#c5ed4d","#44ccff"],
        tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            x : 'center',
            y : 'bottom',
            data: ['民事案件','刑事案件','商事案件','行政案件','执行案件','赔偿案件','知识产权','申请再审']
        },
        series : [
            {
                name: '案件审理数量',
                type: 'pie',
                radius : '60%',
                center: ['50%', '42%'],
                data:[
                    {value:caseCourt[0], name:'民事案件'},
                    {value:caseCourt[1], name:'刑事案件'},
                    {value:caseCourt[2], name:'商事案件'},
                    {value:caseCourt[3], name:'行政案件'},
                    {value:caseCourt[4], name:'执行案件'},
                    {value:caseCourt[5], name:'赔偿案件'},
                    {value:caseCourt[6], name:'知识产权'},
                    {value:caseCourt[7],name:'申请再审'}
                ],
                itemStyle: {
                    emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    });

});