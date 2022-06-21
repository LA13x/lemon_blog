import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/auth/Login'
import Register from '@/components/auth/Register'
import AppIndex from '@/components/home/AppIndex'
import AllArticles from '@/components/home/AllArticles'
import UserHome from '@/components/home/UserHome'
import AdminIndex from '@/components/admin/AppIndex'
import Manage from '@/components/admin/Manage'
import Editor from '@/components/admin/Editor'
import ArticlesModify from '@/components/admin/ArticlesModify'
import ArticleDeatils from '@/components/home/ArticleDetails'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/userhome'
    },
    {
      path: '/home',
      name: 'Home',
      component: Home,
      // home页面并不需要被访问
      redirect: '/index',
      children: [
        {
          path: '/index',
          name: 'AppIndex',
          component: AppIndex,
          redirect: '/userhome',
          meta: {
            requireAuth: true
          }
        },
        {
          // 用户的主页
          path: '/userhome',  
          name: 'UserHome',
          component: UserHome,
          meta: {
            requireAuth: true
          }
        },
        {
          // 所有文章列表
          path: '/allarticles',  
          name: 'AllArticles',
          component: AllArticles,
          meta: {
            requireAuth: true
          }
        },
        {
          // 文章具体内容
          path: '/blog/article',
          name: 'ArticleDeatils',
          component: ArticleDeatils,
          meta: {
            requireAuth: true
          }
        },
      ]
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      // 后台管理
      path: '/admin',
      name: 'AdminIndex',
      component: AdminIndex,
      redirect: '/admin/manage',
      meta: {
        requireAuth: true
      }
    },
    {
      // 文章发布
      path: '/admin/editor',
      name: 'Editor',
      component: Editor,
      meta: {
        requireAuth: true 
      }
    },
    {
      // 文章管理
      path: '/admin/manage',
      name: 'Manage',
      component: Manage,
      meta: {
        requireAuth: true 
      }
    },
    {
      // 文章修改
      path: '/admin/article/modify',
      name: 'ArticlesModify',
      component: ArticlesModify,
      meta: {
        requireAuth: true 
      }
    },
  ]
})
