import React from 'react'
import Date from '../Date'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faUser} from '@fortawesome/free-solid-svg-icons'

const FollowUpUserInfo = ({user, date}) => (
  <div className='d-flex'>
    <div className='bg-secondary mr-2 icon__user'>
      <FontAwesomeIcon color='white' size='lg' icon={faUser}/>
    </div>
    <div>
      <h6>{user.realName}</h6>
      <Date date={date}/>
    </div>
  </div>
)

export default FollowUpUserInfo
