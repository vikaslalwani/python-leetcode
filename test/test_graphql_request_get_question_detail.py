import json
import test.base

from leetcode.models.graphql_query import GraphqlQuery
from leetcode.models.graphql_query_get_question_detail_variables import (
    GraphqlQueryGetQuestionDetailVariables,
)
from leetcode.models.graphql_question_code_snippet import GraphqlQuestionCodeSnippet
from leetcode.models.graphql_question_topic_tag import GraphqlQuestionTopicTag


class TestGraphqlGetQuestionDetail(test.base.BaseTest):
    def test_request(self) -> None:
        graphql_request = GraphqlQuery(
            query="""
                query getQuestionDetail($titleSlug: String!) {
                  question(titleSlug: $titleSlug) {
                    questionId
                    questionFrontendId
                    boundTopicId
                    title
                    frequency
                    freqBar
                    content
                    translatedTitle
                    isPaidOnly
                    difficulty
                    likes
                    dislikes
                    isLiked
                    isFavor
                    similarQuestions
                    contributors {
                      username
                      profileUrl
                      avatarUrl
                      __typename
                    }
                    langToValidPlayground
                    topicTags {
                      name
                      slug
                      translatedName
                      __typename
                    }
                    companyTagStats
                    codeSnippets {
                      lang
                      langSlug
                      code
                      __typename
                    }
                    stats
                    acRate
                    codeDefinition
                    hints
                    solution {
                      id
                      canSeeDetail
                      __typename
                    }
                    hasSolution
                    hasVideoSolution
                    status
                    sampleTestCase
                    enableRunCode
                    metaData
                    translatedContent
                    judgerAvailable
                    judgeType
                    mysqlSchemas
                    enableTestMode
                    envInfo
                    __typename
                  }
                }
            """,
            variables=GraphqlQueryGetQuestionDetailVariables(title_slug="two-sum"),
            operation_name="getQuestionDetail",
        )

        response = self._api_instance.graphql_post(body=graphql_request)

        data = response.data

        assert data

        problemset_question_list = data.problemset_question_list

        assert problemset_question_list is None

        question = data.question
        user = data.user

        assert user is None

        assert question.question_id == "1"
        assert question.question_frontend_id == "1"
        assert question.bound_topic_id is None
        assert question.title == "Two Sum"
        assert question.frequency == 0.0
        assert question.freq_bar > 0
        assert len(question.content) > 10
        assert question.translated_title is None
        assert question.is_paid_only is False
        assert question.difficulty == "Easy"
        assert question.likes > 0
        assert question.dislikes > 0
        assert question.is_liked is None
        assert question.is_favor in (True, False)
        assert json.loads(question.similar_questions)[0]["difficulty"] in (
            "Easy",
            "Medium",
            "Hard",
        )
        assert len(question.contributors) == 0
        assert "python" in list(json.loads(question.lang_to_valid_playground).keys())
        topic_tag = question.topic_tags[0]
        assert isinstance(topic_tag, GraphqlQuestionTopicTag)
        assert len(topic_tag.name) > 0
        assert len(topic_tag.slug) > 0
        assert question.topic_tags[0].translated_name is None
        assert len(topic_tag.typename) > 0

        tag_stat = list(json.loads(question.company_tag_stats).values())[0][0]

        assert tag_stat["taggedByAdmin"] in (True, False)
        assert len(tag_stat["name"]) > 0
        assert len(tag_stat["slug"]) > 0
        assert tag_stat["timesEncountered"] > 0

        code_snippet = question.code_snippets[0]

        assert isinstance(code_snippet, GraphqlQuestionCodeSnippet)
        assert len(code_snippet.code) > 0
        assert len(code_snippet.lang) > 0
        assert len(code_snippet.lang_slug) > 0
        assert code_snippet.typename == "CodeSnippetNode"

        stats = json.loads(question.stats)

        assert len(stats["totalAccepted"]) > 0
        assert len(stats["totalSubmission"]) > 0
        assert int(stats["totalAcceptedRaw"]) > 0
        assert int(stats["totalSubmissionRaw"]) > 0

        assert question.ac_rate > 0

        code_definition = json.loads(question.code_definition)[0]

        assert len(code_definition["value"]) > 0
        assert len(code_definition["text"]) > 0
        assert len(code_definition["defaultCode"]) > 0

        assert [len(hint) > 0 for hint in question.hints]

        solution = question.solution

        # FIXME: this check doesn't work with swagger generated code
        # assert isinstance(solution, GraphqlQuestionSolution)

        # FIXME: swagger generates the code which returns dict
        assert solution["__typename"] == "ArticleNode"
        assert solution["canSeeDetail"] in (True, False)
        assert int(solution["id"]) > 0

        assert question.has_solution in (True, False)
        assert question.has_video_solution in (True, False)

        assert question.status in ("ac", "not_started", "tried")

        assert len(question.sample_test_case) > 0

        assert question.enable_run_code in (True, False)

        meta_data = json.loads(question.meta_data)

        assert meta_data["name"] == "twoSum"
        assert meta_data["params"][0]["name"]
        assert meta_data["params"][0]["type"]
        assert meta_data["return"]["type"]
        assert meta_data["return"]["size"]
        assert meta_data["manual"] in (True, False)

        assert question.translated_content is None

        assert question.judger_available is True
        assert question.judge_type in ("large", "small")

        assert question.mysql_schemas == []

        assert question.enable_test_mode in (True, False)

        env_info = json.loads(question.env_info)

        assert env_info["cpp"][0] == "C++"
