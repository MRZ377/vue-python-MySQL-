import {createRouter, createWebHistory} from 'vue-router'
import IndexView from '@/components/IndexView.vue'
import BookDetailView from '@/components/BookDetailView.vue';
import SearchView from '@/components/SearchView.vue';
import TopView from '@/components/TopView.vue';
import CategoryView from '@/components/CategoryView.vue';
import LoginView from '@/components/LoginView.vue';
import RegisterView from '@/components/RegisterView.vue';
import AddBookInfoView from '@/components/AddBookInfoView.vue';
import DelBookView from '@/components/DelBookView.vue';
import AddChapterView from '@/components/AddChapterView.vue';
import ContentView from '@/components/ContentView.vue';

const routes = [
    {path:'/', component:IndexView, name:'index'},
    {path:'/book/:bookid', component:BookDetailView, name:'bookdetail'},
    {path:'/search', component:SearchView, name:'search'},
    {path:'/top', component:TopView, name:'top'},
    {path:'/categories/:category',component:CategoryView, name:'categories', props:true},
    {path:'/login', component:LoginView, name:'login'},
    {path:'/register', component:RegisterView, name:'register'},
    {path:'/addbook', component:AddBookInfoView, name:'addbook'},
    {path:'/delbook', component:DelBookView, name:'delbook'},
    {path:'/addchapter', component:AddChapterView, name:'addchapter'},
    {path:'/books/:bookid(\\d+)/:chapter_no(\\d+)', component:ContentView, name:'content'}
]

const router = createRouter({
    history:createWebHistory(),
    routes: routes
})

export default router;