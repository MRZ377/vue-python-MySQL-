<template>
    <div class="wrap">
        <div class="login">
            <h2>用户注册</h2>
            <form @submit.prevent="handleRegister">
                <label for="user">账号：</label>
                <input type="text" class="user" v-model="form.username" placeholder="输入账号">
                <label for="password">密码：</label>
                <input type="password" class="password" v-model="form.password" placeholder="输入密码">
                <label for="password">重复密码：</label>
                <input type="password" class="password" v-model="form.repassword" placeholder="再次输入密码">
                 <button type="submit" class="btn_login">确认注册</button>
            </form>
            <router-link to="/login">已有账号，点击登录</router-link>
        </div>
    </div>
</template>

<script setup>
import { useStore } from 'vuex';
import { reactive } from 'vue';
import { useRouter } from 'vue-router';

const store = useStore()
const router = useRouter()
const form = reactive({
    username:'',
    password:'',
    repassword:''
})

async function handleRegister() {
    if(!form.username || !form.password) return alert('用户名或密码为空')
    if (form.password !== form.repassword) return alert('两次输入的密码不一致')
    const res = await store.dispatch('Register',{
        username:form.username,
        password:form.password
    })
    if(res.message === '注册成功'){
        alert('注册成功')
        router.replace('/login')
    }else{
        alert(res.message)
        }
}
</script>

<style scoped>
.login a{
    display: block;
    width: 80%;
    text-align: center;
    background: none repeat scroll rgb(164, 218, 234);
    margin-left: 10%;
    font-size: 25px;
    border-radius: 5px;
    text-decoration: none;
    color: white;
    margin-top: 5%;
    margin-bottom: 5%;
}
.login button{
    display: block;
    align-items: center;
    justify-content: center;
    width: 80%;
    background: none repeat scroll rgb(164, 218, 234);
    margin-left: 10%;
    margin-top: 5%;
    margin-bottom: 5px;
    border: none;
    border-radius: 5px;
    font-size: 25px;
    color: white;
}
.login form input{
    margin: 5px 10%;
    height: 29px;
}
.login form label{
    margin: 5px 10%;
    font-size: 22px;
}
.login form{
    display: flex;
    flex-direction: column;
}
.login h2{
    width: 100%;
    background-color: rgb(41, 150, 223);
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0;
    height: 60px;
    color: azure;
    border-radius: 15px 15px 0px 0px;
    margin-bottom: 20px;
}
.login{
    display: block;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 70%;
    margin: 20px auto;
    background: none repeat scroll white;
    border: 3px solid rgb(181, 227, 237);
    border-radius: 15px;
    height: 500px;
}
</style>