import React, {useEffect, useState} from 'react'
import {HeartButton, CreateButton, SaveButton, CancelButton} from '../buttons'
import {Card} from 'reactstrap'
import Date from '../Date'
import {Content, EditContent} from '../content'
import {FollowUpCard} from '../followups'

const ChatDetail = ({chat, followUps, createFollowUp, updateFollowUp}) => {
  const [addFollowUpMode, toggleAddFollowUpMode] = useState(false)
  const [followUpContent, updateFollowUpContent] = useState("")

  const saveNewFollowUp = () => {
    createFollowUp(chat.id, {content: followUpContent})
    toggleAddFollowUpMode(false)
  }

  const scrollToAddFollowUp = () => {
    Promise.resolve(toggleAddFollowUpMode(true)).then(() =>
      window.scrollTo(0, document.body.scrollHeight)
    )
  }
  /*
   * Scrolls to the top of the page when the component is mounted. Sticky navbar causes a bug that keeps the scroll
   * position when navigating to the chat detail.
   */
  useEffect(() => {
    window.scrollTo(0, 0)
  }, [])

  if (chat) {
    return (
      <Card body className='mb-3 border-0 shadow-sm'>
        <h3 className='mr-3'>{chat.title}</h3>
        <Date className='text-secondary' date={chat.date}/>
        {chat.description ? <Content className='mb-4' source={chat.description}/> : null}
        <div className='mb-4'>
          <HeartButton className='mr-2' count={followUps.length}/>
          <CreateButton type='Follow Up' onClick={scrollToAddFollowUp}/>
        </div>
        <h5 className="mb-3">{followUps.length} Follow Ups</h5>
        {followUps.map((followUp, i) => <FollowUpCard key={i} followUp={followUp} updateFollowUp={updateFollowUp}/>)}
        <hr/>
        {addFollowUpMode ?
          <div>
            <h5>Add New Follow Up:</h5>
            <EditContent content={followUpContent} onChange={updateFollowUpContent}/>
            <div className='mt-2'>
              <SaveButton type='Follow Up' onClick={saveNewFollowUp}/>
              <CancelButton className='ml-2' onClick={() => toggleAddFollowUpMode(false)}/>
            </div>
          </div> :
          <CreateButton type='Follow Up' onClick={scrollToAddFollowUp}/>
        }
      </Card>
    )
  } else {
    return <h1>Loading...</h1>
  }
}

export default ChatDetail
