<template>
  <div class="articles-area">
    <el-card style="text-align: left;width: 990px;margin: 35px auto 0 auto">
      <div>
        <span style="font-size: 20px"><strong>{{article.title}}</strong></span>
        <el-divider content-position="left">{{article.date}}</el-divider>
        <div class="markdown-body">
          <div v-html="article.html"></div>
        </div>
      </div>
    </el-card>
    <el-divider></el-divider>
    <el-card style="text-align: left;width: 990px;margin: 35px auto 0 auto">
        <h3>发表评论（{{ Object.keys(this.comments).length }}）</h3>
        <el-divider></el-divider>
        <el-input
        type="textarea"
        :rows="2"
        placeholder="请输入内容"
        v-model="comment">
        </el-input>
        <el-divider></el-divider>

         <el-popover
        placement="bottom"
        width="200"
        trigger="click"
        :content="msg">
            <el-button  slot="reference" type="primary" @click="onSubmit">评论</el-button>
        </el-popover>
    </el-card>

    <el-card style="text-align: left;width: 990px;margin: 35px auto 0 auto">
        <div v-for="comment_item in comments" :key="comment_item.comment_id" class="comment_item">
            <el-divider content-position="left">用户：{{ comment_item.comment_user }}</el-divider>
                <p>{{ comment_item.comment_content }}</p>
            <el-divider content-position="right">{{ comment_item.comment_date }}</el-divider>
        </div>
    </el-card>

  </div>
</template>

<script>
  export default {
    name: 'ArticleDetails',
    data () {
      return {
        article: [],
        comment: '',
        msg: '',
        comments: []
      }
    },
    mounted () {
      this.loadArticle(),
      this.loadComments()
    },
    methods: {
      loadArticle () {
        var _this = this
        this.$axios.get('/article/' + this.$route.query.id).then(resp => {
          if (resp && resp.data.code == 200) {
            _this.article = resp.data.article
            console.log(resp.data.article);
          }
        })
      },
      onSubmit() {
        // 提交评论
        var _this = this
        this.$axios.post('/comment', {
            user: window.localStorage.getItem('user'),
            article_id: this.$route.query.id,
            comment: this.comment,
        })
        .then(resp=>{
            if (resp && resp.data.code == 200) {
                _this.msg = resp.data.message
                _this.comment = ''
                location.reload()
            } else {
                 _this.msg = resp.data.message
            }
        })
      },
      loadComments() {
        // 加载该文章的所有评论
        var _this = this
        this.$axios.get('/comment/' + this.$route.query.id).then(resp => {
          if (resp && resp.data.code == 200) {
            _this.comments = resp.data.comments
          }
        })
      }
    }
  }
</script>

<style scoped>
  @import "../../styles/markdown.css";
  .comment_item {
      padding: 24px;
  }
</style>

