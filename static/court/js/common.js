$(function(){
	// 搜索框按钮
	$('.search-btn').click(function(){
		$(this).animate({
			"left": "250px"
		},300);
		$(".search-container").animate({
			"left": "0px"
		},300);
		$(".search-container").find('.search-content').focus();
	});

	// 视频弹窗
	$(".court-videos").click(function(){
		layer.open({
			type: 2,
			title: '达州市城市宣传片',
			content: "http://player.youku.com/player.php/sid/XODM1MzAxMDg4/v.swf",
			area: ['500px', '500px']
		}); 
	});

	// 幻灯片
	$.fn.bannerPlayer = function(){
		var _this = $(this); // 缓存容器
		var _index = 5; // 记录滑块索引
		var _time = 3000; // 切换间隔
		var move = function(){				
			if (_index == 11) {
				_this.find('.news-list').css({
					"left" : "-3750px"
				});
				_index = 6; 
			}
			if (_index == 3){
				_this.find('.news-list').css({
					"left" : "-6750px"
				});
				_index = 8;
			}
			_this.find('.news-list').stop().animate({
				"left" : "-" + _index * 750 + "px"
			},600);
		}; 

		_this.find('.news-list').html(
			_this.find('.news-list').html() 
			+ _this.find('.news-list').html()
			+ _this.find('.news-list').html()
		);

		var palyerTimer = setInterval(function(){
			_index += 1;
			move();
		},_time);

		_this.hover(function(){
			clearInterval(palyerTimer);
		},function(){
			palyerTimer = setInterval(function(){
				_index += 1;
				move();
			},_time);
		});

		$('.prev-btn').click(function(){
			_index--;
			move();
		});
		
		$('.next-btn').click(function(){
			_index++;
			move();
		});
	};
	$('.banner-container').bannerPlayer();

	//  加入收藏 
	function AddFavorite(sURL, sTitle){
	    try{
	        window.external.addFavorite(sURL, sTitle);
	    }
	    catch (e){
	        try{
	            window.sidebar.addPanel(sTitle, sURL, "");
	        }
	        catch (e){
	            alert("加入收藏失败，请使用Ctrl+D进行添加");
	        }
	    }
	}
	
	//  设为首页
	function SetHome(obj,vrl){
	        try{
                obj.style.behavior='url(#default#homepage)';obj.setHomePage(vrl);
	        }
	        catch(e){
                if(window.netscape) {
                    try {
                        netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
                    }
                    catch (e) {
                        alert("此操作被浏览器拒绝！\n请在浏览器地址栏输入“about:config”并回车\n然后将 [signed.applets.codebase_principal_support]的值设置为'true',双击即可。");
                    }
                    var prefs = Components.classes['@mozilla.org/preferences-service;1'].getService(Components.interfaces.nsIPrefBranch);
                    prefs.setCharPref('browser.startup.homepage',vrl);
                 }
	        }
	}

});