<template>
    <div class="warp">
        <div class="addbookinfo">
            <h2>添加书籍</h2>
            <form @submit.prevent="handleSubmit()">
                <label for="">书名：</label>
                <input type="text" v-model="form.bookname">
                <label for="">作者：</label>
                <input type="text" v-model="form.author">
                <label for="">封面（图片路径的方式提供）：</label>
                <input type="text" v-model="form.bookimage">
                <label for="">类别：</label>
                <input type="text" v-model="form.category">
                <label for="">书籍简介：</label>
                <input type="text" v-model="form.bookinfo">
                <button type="submit">提交</button>
            </form>
        </div>
    </div>
</template>

<script setup>
import { reactive } from 'vue';
import { useStore } from 'vuex';

const store = useStore()
const form = reactive({
    bookname: '',
    author: '',
    bookimage: '',
    category: '',
    bookinfo: ''
})

async function handleSubmit() {
    try{
        const res = await store.dispatch('addBook', form)
        alert(res.message || '添加成功')
        Object.keys(form).forEach(k => form[k] = '')
    }catch(e){
        alert(e?.response?.data?.message || '添加失败')
    }
}

</script>

<style scoped>
.addbookinfo form button{
    height: 40px;
    font-size: 24px;
    margin: 10px;
    border: none;
    background: none repeat scroll rgb(130, 196, 244);
    color: white;
}
.addbookinfo form input{
    height: 26px;
    margin: 10px;
}
.addbookinfo form label{
    font-size: 20px;
    color: rgb(92, 111, 111);
    margin: 10px;
}
.addbookinfo form{
    display: flex;
    flex-direction: column;
    
}
.addbookinfo h2{
    margin: 0;
    display: flex;
    align-items: center;
    height: 40px;
    justify-content: center;
    width: 100%;
    color: white;
    font-weight: 500;
    font-size: 26px;
    background: none repeat scroll rgb(80, 161, 162);
    border-radius: 12px 12px 0px 0px;
}
.addbookinfo{
    display: block;
    margin: 10px;
    border: 3px solid rgb(118, 159, 160);
    padding-bottom: 10px;
    border-radius: 15px;
}
</style>