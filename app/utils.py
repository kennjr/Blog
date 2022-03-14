from datetime import datetime
import time

from app.models import Comment


def format_default_timestamp_single(user_item):
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")


def convert_ids_string_to_array(ids_str: str):
    if ids_str != "":
        ids_array = []
        split_str = ids_str.split(",")
        for item in split_str:
            if item != "" and item.isnumeric():
                ids_array.append(int(item.strip()))
    else:
        ids_array = []
    return ids_array


def convert_ids_array_to_string(ids_array: list):
    global ids_str
    if ids_array:
        ids_str = ""
        for my_id in ids_array:
            ids_str += f",{my_id}"

    return ids_str


def format_blogs_array(blogs_array):
    if blogs_array:
        from app.models import Blog
        formatted_pitches_array = []
        for blog in blogs_array:
            blog_txt = blog.blog_txt
            blog_title = blog.title
            blog_description = blog.description
            blog_saves = blog.saves
            blog_timestamp = blog.timestamp
            blog_creator_id = blog.creator_id
            blog_comments = len(convert_ids_string_to_array(blog.comments))

            formatted_pitch = Blog(id=blog.id, blog_txt=blog_txt, comments=blog_comments,
                                   timestamp=blog_timestamp, description=blog_description, saves=blog_saves,
                                   creator_id=blog_creator_id, title=blog_title)
            formatted_pitches_array.append(formatted_pitch)
        return formatted_pitches_array
    else:
        return blogs_array


def format_comments_array(comments_array):
    if comments_array:

        formatted_comments_array = []
        for comment in comments_array:
            blog_id = comment.blog_id
            comment_txt = comment.comment_txt
            creator_id = comment.creator_id
            timestamp = comment.timestamp

            formatted_comment = Comment(id=comment.id, comment_txt=comment_txt, creator_id=creator_id, blog_id=blog_id,
                                        timestamp=timestamp)

            formatted_comments_array.append(formatted_comment)
        return formatted_comments_array
    else:
        return []
