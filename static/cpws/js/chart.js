$(function(){
	var myChart = echarts.init(document.getElementById('chart1'));
    var myChart2 = echarts.init(document.getElementById('chart2'));
    // 文书数量分布
    var documentData = [20198,5535,12321,1554,1124];
    // 历年文书走势
    var documentDataYear = [447,9422,14512,2532];
    

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption({
        title: {
            text: '文书数量分布图',
            textStyle: {
	            color: "#195caa",
	            fontWeight: "bold",
	            textAlign: "center",
	            fontSize: 20
            },
            x: 'center',
        	y: 10
        },
        tooltip: {},
        legend: {
        	show: true,
        	left: 10,
            data:['销量']
        },
        xAxis: {
            data: ["民事案件","刑事案件","行政案件","执行案件","赔偿案件"],
        	axisTick: {
        		show: false
        	},
        	splitLine: {
        		show: false
        	}
        },
        yAxis: {
        	axisLine: {
        		show: false
        	},
        	axisTick: {
        		show: false
        	},
        	axisLabel: {
        		textStyle: {
        			color: "#195caa"
        		}
        	}
        },
        series: [{
            type: 'bar',
            name: "文书数量",
            barWidth: 50,
            data: [
	            {
	            	value: documentData[0],
	            	itemStyle:{
	            		normal:{color:'#485c89'}
	            	},
	            	label:{
	            		normal:{
	            			show:true,
	            			position:"top",
	            			textStyle:{color:"#000000"}
	            		}
	            	}
	            },
	            {
	            	value: documentData[1],
	            	itemStyle:{
	            		normal:{color:'#374159'}
	            	},
	            	label:{
	            		normal:{
	            			show:true,
	            			position:"top",
	            			textStyle:{color:"#000000"}
	            		}
	            	}
	            },
	            {
	            	value: documentData[2],
	            	itemStyle:{
	            		normal:{color:'#405789'}
	            	},
	            	label:{
	            		normal:{
	            			show:true,
	            			position:"top",
	            			textStyle:{color:"#000000"}
	            		}
	            	}
	            },
	            {
	            	value: documentData[3],
	            	itemStyle:{
	            		normal:{color:'#b0c1e4'}
	            	},
	            	label:{
	            		normal:{
	            			show:true,
	            			position:"top",
	            			textStyle:{color:"#000000"}
	            		}
	            	}
	            },
	            {
	            	value: documentData[4],
	            	itemStyle:{
	            		normal:{color:'#20293d'}
	            	},
	            	label:{
	            		normal:{
	            			show:true,
	            			position:"top",
	            			textStyle:{color:"#000000"}
	            		}
	            	}
	            }
            ],
            animationDuration: 800,
            animationEasing: "ease"
        }]
    });

    myChart2.setOption({
        title: {
            text: '文书公布数量趋势图',
            textStyle: {
	            color: "#195caa",
	            fontWeight: "bold",
	            textAlign: "center",
	            fontSize: 20
            },
            x: 'center',
        	y: 10
        },
        tooltip: {
        	trigger: 'axis'
        },
        legend: {
        	show: true,
        	left: 10,
            data:['销量']
        },
        xAxis: {
            data: ["2013","2014","2015","2016",],
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
        	},
        	axisLabel: {
        		textStyle: {
        			color: "#195caa"
        		}
        	}
        },
        series: [{
            type: 'line',
            name: "文书数量",
            smooth: true,
            symbolSize: 10,
            lineStyle: {
            	normal: {
            		color: "#5275c3",
            		width: 5
            	}
            },
            data: [
	            {
	            	value: documentDataYear[0],
	            	itemStyle:{
	            		normal:{color:'#485c89'}
	            	}
	            },
	            {
	            	value: documentDataYear[1],
	            	itemStyle:{
	            		normal:{color:'#374159'}
	            	}
	            },
	            {
	            	value: documentDataYear[2],
	            	itemStyle:{
	            		normal:{color:'#405789'}
	            	}
	            },
	            {
	            	value: documentDataYear[3],
	            	itemStyle:{
	            		normal:{color:'#b0c1e4'}
	            	}
	            }
            ]
        }]
    });
	
});