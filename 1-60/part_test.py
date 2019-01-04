#coding=utf-8
def read_squad_examples(is_training=1):
  """Read a SQuAD json file into a list of SquadExample."""
  input_data={"article_content": "然而无论剧情如何变化，角色如何增减，《冰河世纪》的金字招牌仍旧还是那只对坚果怀有惊人狂热激情的犬齿松鼠斯科特。在《冰河世纪2》的预告片中，斯科特和它的坚果再次担纲主演，为了榛子不惜上山下海挑战极限，还要和大鱼比划功夫……   影片资料   更多外文名：iceage3.。。。。usa(workingtitle)   国家/地区：美国   类型：喜剧/动画/冒险   对白语言：英语", "questions": [{"answer_start": 192, "question": "《冰河世纪》的语言是什么？", "answer": "英语"}]}
  symbol=["！","？",'｡','＂','＃','＄','％','＆','＇','（','）','＊','＋','，','－','／','/','：','；',
  '＜','＝','＞','＠','［','＼','］','＾','＿','｀','｛','｜','｝','～','｟','｠','｢','｣','､','、',
  '〃','》','「','」','『','』','【','】','〔','〕','〖','〗','〘','〙','〚','〛','〜','〝','〞','〟',
  '〰','〾','〿','–','—','‘','‛','“','”','„','‟','…','\'']
  def is_whitespace(c):#虽然没有先添加空格，但是因为中文字段中经常性的存在空格，没什么意义，而且关键还占字节位置
    if c == " " or c == "\t" or c == "\r" or c == "\n" or ord(c) == 0x202F:
      return True
    return False
  def create_chinese_symbol_dct():
      dct=dict.fromkeys(symbol,0)
      return dct
  chines_symbol=create_chinese_symbol_dct()
  examples = []
  count=0
  paragraph=input_data
  paragraph_text = paragraph["article_content"]
  doc_tokens = []
  char_to_word_offset = []
  for c in paragraph_text:
    if is_whitespace(c):
      prev_is_whitespace = True
    elif c in chines_symbol:
      if not doc_tokens:
        doc_tokens.append(c)
      else:
        doc_tokens[-1] += c
    else:
        #if prev_is_whitespace:
      doc_tokens.append(c)#save words without whitespace
        #else:
          #doc_tokens[-1] += c #speci-\nal
        #prev_is_whitespace = False
    char_to_word_offset.append(len(doc_tokens) - 1)
     #这么说，start_position和end _position之间的单词可能和origin_answer_text不一样。
        #temp.append(doc_tokens)
      #char_to_word_offset.append(doc_tokens)
      #del whitespace in context para and contact them
  for qa in paragraph["questions"]:
    #qa is a dict
    qas_id = "question_id"+str(count)
    count+=1
    question_text = qa["question"]
    start_position = None
    end_position = None
    orig_answer_text = None
    is_impossible = False
    if is_training:
      is_impossible = False
      #if (len(qa["answer"]) != 1) and (not is_impossible):
      #  raise ValueError(
      #      "For training, each question should have exactly 1 answer.")
      if not is_impossible:
        orig_answer_text = qa["answer"]
        answer_offset = qa["answer_start"]
        answer_length = len(orig_answer_text)
        print(orig_answer_text)
        print(len(char_to_word_offset))
        print(answer_offset)
        print(paragraph_text)
        print(doc_tokens)
        print(len(doc_tokens))
        start_position = char_to_word_offset[answer_offset]
        #中文数据有一些错误
        #表示去除了空格,标点靠前后，在doc_tokens中的位置
        #start_position=answer_offset
        if (answer_offset + answer_length -1)>=len(char_to_word_offset):
          break
        else:
          end_position = char_to_word_offset[answer_offset + answer_length -1]
  return
read_squad_examples()