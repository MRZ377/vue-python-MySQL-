import {createStore} from 'vuex'
import axios from 'axios'
import router from '@/router/router';

export default createStore({
    state:{
        loginstate:false,
        user:null
    },
    mutations:{
        setLoginState(state, value){
            state.loginstate = value;
            if(!value) state.user =null
            localStorage.setItem('loginState', value ? '1' : '')
        },
        setUser(state, payload){
            state.user = payload
            localStorage.setItem('user', JSON.stringify(payload))
        },
        restoreUser(state){
            const u = localStorage.getItem('user')
            if (u){
                state.user = JSON.parse(u)
                state.loginstate = true
            }
        }
    },
    getters:{
        getLoginState:(state) => state.loginstate,
        getUser:(state) =>state.user
    },
    actions:{
        /**
         * 获取时间排序章节
         * @returns {Primise}
         */
        async getchaptertime(){
            const {data} = await axios.get('/api/chaptertime')
            return data
        },
        /**
         * 获取时间排序书籍
         * @returns {Primise} 
         */
        async gettime(){
            const {data} = await axios.get('/api/timelist')
            return data
        },
        /**
         * 获取内容
         * @param {*} 
         * @param {{bookid:number,chapter_no:number}} payload
         * @returns {Primise}  
         */
        async getContent(_, {bookid, chapter_no}){
            const data = await axios.get(`/api/content/${bookid}/${chapter_no}`)
            return data
        },
        /**
         * 添加章节
         * @param {*}
         * @param {Object}
         * @returns {Primise} 
         */
        async addChapter(_, fd){
            const {data} = await axios.post('/api/addchapter', fd,{headers:{'Content-Type':'multipart/form-data'}})
            return data
        },
        /**
         * 详情页数据
         * @param {*} context
         * @param {Object}
         * @returns {Primise}  
         */
        async getDetail(_, bookid){
            const {data:bookinfo} = await axios.get(`/api/book/${bookid}`)
            const {data:chapterlist} = await axios.get(`/api/content/${bookid}`)
            return {bookinfo, chapterlist} 
        },
        /**
         * 书籍详情
         * @param {*} context 
         * @param {*} payload 
         * @returns 
         */
        async openDetail(_,bookid){
            const [bookinfo, chapters] = await Promise.all([
                axios.get(`/api/book/${bookid}`),
                axios.get(`/api/content/${bookid}`)
            ])
            const info = bookinfo.data
            const chapterlist = chapters.data
            router.push({
                name:'bookdetail',
                params:{bookid},
                state:{info, list:chapterlist}
            })
            return info
        },
        /** 
        *添加书籍
        *@param {*}
        *@param {Object}
        *@returns {Primise}
        */ 
       async addBook(context,payload){
        const {data} = await axios.post('/api/addbook', payload)
        return data
       },
       /**
        * 删除书籍
        * @param {*}
        * @param {Object}
        * @returns {Primise}
        */
       async delBook(context, payload){
        const {data} = await axios.post('/api/delbook', payload)
        return data
       },
       /**
       *获取书籍列表
       *@returns Promise<list[dict]>
       */
       async getBookList(){
        const {data} = await axios.get('/api/books')
        return data
       },
       /** 
       *搜索书籍
       *@param {*}
       *@returns {Primise}
       */
      async getSearchBook(_,q){
        const {data} = await axios.get('/api/search',{params:{q}})
        return data
      },
      /**
      *类别书籍
      *@param {*}
      *@returns {Primise}
      */
     async getCategory(_, category){
        const {data} = await axios.get('/api/categories', {params:{category}})
        return data
     },
     /** 
     *排行榜书籍(按类别分类)
     *@retruns {Primise}
     */
    async getTopBook(){
        const {data} = await axios.get('/api/top')
        return data
    },
    /**
     * 登录接口
     * @param {{username:string, password:string}} payload
     * @returns {Primise}
     */
    async Login({commit}, payload){
        const {data} = await axios.post('/api/login', payload)
        if (data.message === '登录成功'){
            commit('setLoginState', true);
            commit('setUser', {username: data.username, Permission:data.Permission})
        }else{
            commit('setLoginState', false)
        }
        return data
    },
    /**
     * 注册接口
     * @param {{username:string, password:string}} payload
     * @returns {Primise}
     */
    async Register(_, payload){
        const {data} = await axios.post('/api/register', payload)
        return data
    }
    }
});