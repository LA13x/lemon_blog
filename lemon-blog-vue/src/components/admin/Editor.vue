<template>
  <div>
    <AdminNav></AdminNav>
    <el-row style="margin: 18px 0px 0px 18px ">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item>文章发布</el-breadcrumb-item>
      </el-breadcrumb>
    </el-row>
    <el-row>
      <el-input
        v-model="article.articleTitle"
        style="margin: 10px 0px;font-size: 18px;"
        placeholder="请输入标题"></el-input>
    </el-row>
    <el-row style="height: calc(100vh - 140px);">
      <mavon-editor
        v-model="article.articleContentMd"
        style="height: 100%;"
        ref=md
        @save="saveArticles"
        fontSize="16px">
        <button type="button" class="op-icon el-icon-document" :title="'摘要'" slot="left-toolbar-after"
                @click="dialogVisible = true"></button>
      </mavon-editor>
      <el-dialog
        :visible.sync="dialogVisible"
        width="30%">
        <el-divider content-position="left">摘要</el-divider>
        <el-input
          type="textarea"
          v-model="article.articleAbstract"
          rows="6"
          maxlength="255"
          show-word-limit></el-input>
          
        
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
  </div>
</template>

<script>
    import AdminNav from '../common/AdminNav'
    export default {
        name: 'Editor',
        components: {AdminNav},
        data () {
        return {
            article: {},
            dialogVisible: false,
            fileList: []
        }
        },
        mounted () {
        if (this.$route.params.article) {
            this.article = this.$route.params.article
        }
        },
        methods: {
        saveArticles (value, render) {
            // value 是 md，render 是 html
            console.log(value, render);
            this.$confirm('是否保存并发布文章?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
            }).then(() => {
                console.log(this.article.id);
                console.log(this.article.articleTitle);
                console.log(value);
                this.$axios
                .post('/post/article', {
                    id: this.article.id,
                    // id: 1,
                    articleTitle: this.article.articleTitle,
                    articleContentMd: value,
                    articleContentHtml: render,
                    articleAbstract: this.article.articleAbstract,
                    // articleCover: this.article.articleCover,
                    articleDate: this.article.articleDate,
                    username: window.localStorage.getItem('user')
                }).then(resp => {
                if (resp && resp.data.code == 200) {
                    this.$message({
                        type: 'info',
                        message: '已保存成功'
                    })
                    console.log(resp.date);
                } else {
                    console.log(resp.data);
                }
                })
            }
            ).catch(() => {
            this.$message({
                type: 'info',
                message: '已取消发布'
            })
            })
        },
        }
    }
</script>

