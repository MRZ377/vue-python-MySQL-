<template>
      <div class="header-top">
        <div class="wrap">
            <div v-if="!loginstate" class="toplogin">
                <a href="/login">登录</a>
                &nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
                <a href="/register">用户注册</a>
            </div>
            <div v-if="loginstate" class="toplogin">
                欢迎！
                &nbsp;
                {{ user.username }}
                &nbsp;&nbsp;|&nbsp;&nbsp;
                <button style="font-size: 14px;color: orange;" @click="logout">登出</button>
            </div>
        </div>
    </div>
    <div class="header">
        <div class="wrap">
            <div class="logo">
                <a href="/" title="首页">首页</a>
            </div>
            <div class="search">
                <form @submit.prevent="handleSearch">
                    <input type="search" class="text" name="q" placeholder="输入进行搜索" v-model="searchQuery">
                    <input type="submit" class="btn" value>
                </form>
            </div>
            <div class="share">
                <a href="/bookcase.html">阅读记录</a>
            </div>
        </div>
        <div class="nav">
            <ul>
                <li>
                    <a href="/">首页</a>
                </li>
                <li>
                    <router-link :to="{name:'categories', params:{category:'玄幻'}}">玄幻</router-link>
                </li>
                <li>
                    <router-link :to="{name:'categories', params:{category:'科幻'}}">科幻</router-link>
                </li>
                <li>
                    <router-link :to="{name:'categories', params:{category:'男生'}}">男生</router-link>
                </li>
                <li>
                    <router-link :to="{name:'categories', params:{category:'历史'}}">历史</router-link>
                </li>
                <li>
                    <router-link :to="{name:'categories', params:{category:'武侠'}}">武侠</router-link>
                </li>
                <li>
                    <router-link :to="{name:'categories', params:{category:'都市'}}">都市</router-link>
                </li>
                <li>
                    <router-link :to="{name:'categories', params:{category:'女生'}}">女生</router-link>
                </li>
                <li>
                    <router-link :to="{name:'categories', params:{category:'完结'}}">完结</router-link>
                </li>
                <li>
                    <a href="/top">排行榜</a>
                </li>
            </ul>
        </div>
    </div>
  <router-view :key="$route.fullPath"></router-view>
</template>

<script>
import { mapGetters } from 'vuex';

export default{
  data(){
    return{
        searchQuery: ''
    }
  },
    computed:{
        ...mapGetters(['getLoginState', 'getUser']),
        loginstate(){
            return this.getLoginState;
        },
        user(){
            return this.getUser || {};
        }
    },
    
    methods:{
        handleSearch(){
            if(this.searchQuery.trim() === ''){
                alert('请先输入');
                return;
            }
            this.$router.push({path:'/search', query:{q:this.searchQuery}});
        },
        logout() {
            this.$store.commit('setLoginState', false)
            this.$store.commit('setUser', null)
            localStorage.removeItem('loginState')
            localStorage.removeItem('user')
        },
    },
}
</script>

<style>
body.dark{background: #121212; color: #eee;}
body.eye{background: #e8f5e9; color: #2e7d32;}
.share a:hover{
    color: orange;
}
.share a{
    text-decoration: none;
}
body{
    background-color: #d1e6f0;
}
.nav{
    background-color: #88c6E5;
}
.nav ul{
    list-style: none;
    padding: 0;
    margin: 0;
    overflow: hidden;
    text-align: center;
}
.nav ul li{
    display: inline-block;
    margin: 0 15px;
}
.nav ul li a{
    text-decoration: none;
    color: white;
    font-size: 16px;
    padding: 10px 15px;
    display: block;
}
.nav ul li a:hover{
    background-color: #6699CC;
}
.item{
    float:left;
    width:50%;
    height:156px;
    margin-bottom:10px;
    position:relative;
    overflow:hidden;
}.class .item{width:33.3%;}
.item .image{
    position:absolute;
    top:0px;
    left:5px;
}
.item .image img{
    width:120px;
    height:150px;
    background-color:#FFF;
    border:1px solid #DDD;
    padding:1px;
}
.item dl{
    padding-left:140px;
    padding-right:5px;
}
.item dl dt{
    border-bottom:1px dotted #A6D3E8;
    font-size:14px;
    font-weight:700;
    height:25px;
    line-height:25px;
    overflow:hidden;
}
.item dl dt span{
    color:#999;
    float:right;
    font-weight:400;
}
.item dl dd{
    height:120px;
    line-height:20px;
    overflow:hidden;
    padding:7px 0 0;
    color:#AAA;
}
.item dl dt a{
    color: #6699CC;
    text-decoration: none;
    font-size: 20px;
}
.header-top{
    margin-bottom:0px;
    background-color:#E1ECED;
    border-bottom:1px solid #A6D3E8;
    color:#999;
    height:30px;
    line-height:30px;
    min-width:980px;
    width:100%;
}
.wrap, .nav{
    width: 980px;
    margin: 0 auto;
    zoom: 1;
    overflow: hidden;
}
.toplogin{
    display: flex;
    justify-content: flex-end;
}
.header-top a{
    color: #888;
}
.header {
    zoom: 1;
    overflow: hidden;
    padding: 10px;
}
.header .wrap{
    height: 60px;
    margin: 10px auto;
}
.header .logo{
    float: left;
}
.logo a{
    font-family: Arial, Helvetica, sans-serif;
    display: block;
    height: 50px;
    width: 200px;
    line-height: 50px;
    color: #0065b5;
    font-size: 36px;
    text-shadow: #8c8989 3px 3px 6px;
    text-decoration: none;
}
.header .search{
    float: left;
    width: 500px;
    overflow: hidden;
}
.search form{
    margin:10px;
    position: relative;
    clear: both;
}
.search .text {
    display: block;
    width:100%;
    padding-left:10px;
    height: 40px;
    line-height:40px;
    overflow: hidden;
    border: 1px solid #ddd;
    border-right:51px solid #fff;
    font-size:14px;
}
.search .btn{
    position: absolute;
    z-index: 1;
    right: 0;
    top: 0;
    margin: 0;
    width: 50px;
    height: 40px;
    border: 1px solid #ddd; 
    background: transparent url(/public/images/so.png) no-repeat 50% 50%;
    -webkit-background-size: 20px 21px;
    -moz-background-size: 20px 21px;
    -o-background-size: 20px 21px;
    background-size: 20px 21px;
    border-radius:0px;
}
.wrap .share{
    float: right;
    border: 1px dotted #ddd;
    margin-top: 10px;
    padding: 6px;
    color: #CCC;
}
</style>
