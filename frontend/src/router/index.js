import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleListView from '../views/ArticleListView.vue'
import ArticleDetailView from '../views/ArticleDetailView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/articlelist',
    name: 'articlelist',
    component: ArticleListView
  },
  {
    path: '/article/:articleId',
    name: 'articledetail',
    component: ArticleDetailView
  },
  {
    path: '/add-article',
    name: 'articlecreate',
    component: ArticleCreateView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
