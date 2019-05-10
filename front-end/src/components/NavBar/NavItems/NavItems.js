// **** mahboobeh salmani ****

import React from 'react';

import classes from './NavItems.module.css';
import NavItem from './NavItem/NavItem';
import Home from '../../../assets/icons/icon-home.png';
import Profile from '../../../assets/icons/icon-profile.png';
import Reserve from '../../../assets/icons/icon-reservation.png';
import NewReview from '../../../assets/icons/icon-newReview.png';

const navItems = () => (
    <ul className={classes.NavItems}>
        <NavItem active link="/" itemImage={Home} content="صفحه اول">صفحه اول</NavItem>
        <NavItem link="/" itemImage={Profile}>پروفایل</NavItem>
        <NavItem link="/" itemImage={Reserve}>رزرو</NavItem>
        <NavItem link="/"  itemImage={NewReview}>ایجاد نقد</NavItem>
    </ul>
);


export default navItems;