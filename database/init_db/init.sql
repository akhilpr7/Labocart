--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE labocart;
--
-- Name: labocart; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE labocart WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_IN' LC_CTYPE = 'en_IN';


\connect labocart

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: authentication_jobmodel; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.authentication_jobmodel (
    id integer NOT NULL,
    job_title character varying(255) NOT NULL,
    category character varying(255) NOT NULL
);


--
-- Name: authentication_jobmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.authentication_jobmodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: authentication_jobmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.authentication_jobmodel_id_seq OWNED BY public.authentication_jobmodel.id;


--
-- Name: authentication_labourmodels; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.authentication_labourmodels (
    id integer NOT NULL,
    username character varying(25) NOT NULL,
    image_link character varying(10000) NOT NULL,
    job_title character varying(50) NOT NULL,
    rate double precision NOT NULL,
    work_type boolean NOT NULL,
    status integer NOT NULL
);


--
-- Name: authentication_labourmodels_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.authentication_labourmodels_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: authentication_labourmodels_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.authentication_labourmodels_id_seq OWNED BY public.authentication_labourmodels.id;


--
-- Name: authentication_newusermodel; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.authentication_newusermodel (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    phone_no character varying(16),
    rating integer NOT NULL,
    is_sub boolean NOT NULL,
    wallet double precision NOT NULL,
    subscribed_at date,
    package integer NOT NULL,
    image character varying(3000)
);


--
-- Name: authentication_newusermodel_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.authentication_newusermodel_groups (
    id integer NOT NULL,
    newusermodel_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- Name: authentication_newusermodel_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.authentication_newusermodel_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: authentication_newusermodel_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.authentication_newusermodel_groups_id_seq OWNED BY public.authentication_newusermodel_groups.id;


--
-- Name: authentication_newusermodel_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.authentication_newusermodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: authentication_newusermodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.authentication_newusermodel_id_seq OWNED BY public.authentication_newusermodel.id;


--
-- Name: authentication_newusermodel_user_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.authentication_newusermodel_user_permissions (
    id integer NOT NULL,
    newusermodel_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: authentication_newusermodel_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.authentication_newusermodel_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: authentication_newusermodel_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.authentication_newusermodel_user_permissions_id_seq OWNED BY public.authentication_newusermodel_user_permissions.id;


--
-- Name: authentication_requests; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.authentication_requests (
    id integer NOT NULL,
    username character varying(255) NOT NULL,
    worker_username character varying(255) NOT NULL,
    status boolean NOT NULL
);


--
-- Name: authentication_requests_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.authentication_requests_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: authentication_requests_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.authentication_requests_id_seq OWNED BY public.authentication_requests.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- Name: ecommerce_cartmodel; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ecommerce_cartmodel (
    id integer NOT NULL,
    product_id integer NOT NULL,
    "Product_name" text NOT NULL,
    "Price" double precision NOT NULL,
    "Total" double precision NOT NULL,
    "Quantity" integer NOT NULL,
    "Image" text NOT NULL,
    username character varying(255) NOT NULL,
    cartnumber integer NOT NULL
);


--
-- Name: ecommerce_cartmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ecommerce_cartmodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ecommerce_cartmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ecommerce_cartmodel_id_seq OWNED BY public.ecommerce_cartmodel.id;


--
-- Name: ecommerce_checkoutmodel; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ecommerce_checkoutmodel (
    id integer NOT NULL,
    product_id integer NOT NULL,
    "Products" text NOT NULL,
    "Total" double precision NOT NULL,
    "Quantity" integer NOT NULL,
    username character varying(255) NOT NULL
);


--
-- Name: ecommerce_checkoutmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ecommerce_checkoutmodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ecommerce_checkoutmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ecommerce_checkoutmodel_id_seq OWNED BY public.ecommerce_checkoutmodel.id;


--
-- Name: ecommerce_hiremodel; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ecommerce_hiremodel (
    id integer NOT NULL,
    worker_name text NOT NULL,
    "Hire_name" text NOT NULL,
    "Name" text NOT NULL,
    "Place" text NOT NULL,
    "Work_mode" character varying(6) NOT NULL,
    "Phone" bigint NOT NULL,
    status integer NOT NULL,
    job_title character varying(20) NOT NULL,
    user_status boolean NOT NULL,
    worker_status boolean NOT NULL,
    rating integer NOT NULL
);


--
-- Name: ecommerce_hiremodel_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ecommerce_hiremodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ecommerce_hiremodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ecommerce_hiremodel_id_seq OWNED BY public.ecommerce_hiremodel.id;


--
-- Name: ecommerce_packagemodel; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ecommerce_packagemodel (
    id integer NOT NULL,
    package_name character varying(50) NOT NULL,
    validity integer NOT NULL,
    cost double precision NOT NULL,
    image text NOT NULL
);


--
-- Name: ecommerce_packagemodel_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ecommerce_packagemodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ecommerce_packagemodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ecommerce_packagemodel_id_seq OWNED BY public.ecommerce_packagemodel.id;


--
-- Name: ecommerce_productsmodel; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ecommerce_productsmodel (
    id integer NOT NULL,
    "Product_name" text NOT NULL,
    "Price" double precision NOT NULL,
    "Quantity" integer NOT NULL,
    "Image" text NOT NULL
);


--
-- Name: ecommerce_productsmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ecommerce_productsmodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ecommerce_productsmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ecommerce_productsmodel_id_seq OWNED BY public.ecommerce_productsmodel.id;


--
-- Name: ecommerce_purchasemodel; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ecommerce_purchasemodel (
    id integer NOT NULL,
    phone bigint,
    "Total" double precision NOT NULL,
    "Prices" double precision[] NOT NULL,
    "Quantity" integer[] NOT NULL,
    "Product_name" character varying(100)[],
    username character varying(100) NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email text NOT NULL,
    street text NOT NULL,
    building text NOT NULL,
    locality text NOT NULL,
    postal integer NOT NULL,
    status integer,
    order_id integer NOT NULL,
    date date NOT NULL
);


--
-- Name: ecommerce_purchasemodel_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ecommerce_purchasemodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ecommerce_purchasemodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ecommerce_purchasemodel_id_seq OWNED BY public.ecommerce_purchasemodel.id;


--
-- Name: home_category; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.home_category (
    id integer NOT NULL,
    category_name character varying(255) NOT NULL
);


--
-- Name: home_category_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.home_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: home_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.home_category_id_seq OWNED BY public.home_category.id;


--
-- Name: home_transaction; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.home_transaction (
    id integer NOT NULL,
    username character varying(255) NOT NULL,
    product_name character varying(255) NOT NULL,
    total_price integer NOT NULL,
    date date NOT NULL,
    quantity integer NOT NULL,
    "Status" character varying(100) NOT NULL
);


--
-- Name: home_transaction_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.home_transaction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: home_transaction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.home_transaction_id_seq OWNED BY public.home_transaction.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: authentication_jobmodel id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_jobmodel ALTER COLUMN id SET DEFAULT nextval('public.authentication_jobmodel_id_seq'::regclass);


--
-- Name: authentication_labourmodels id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_labourmodels ALTER COLUMN id SET DEFAULT nextval('public.authentication_labourmodels_id_seq'::regclass);


--
-- Name: authentication_newusermodel id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_newusermodel ALTER COLUMN id SET DEFAULT nextval('public.authentication_newusermodel_id_seq'::regclass);


--
-- Name: authentication_newusermodel_groups id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_newusermodel_groups ALTER COLUMN id SET DEFAULT nextval('public.authentication_newusermodel_groups_id_seq'::regclass);


--
-- Name: authentication_newusermodel_user_permissions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_newusermodel_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.authentication_newusermodel_user_permissions_id_seq'::regclass);


--
-- Name: authentication_requests id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_requests ALTER COLUMN id SET DEFAULT nextval('public.authentication_requests_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: ecommerce_cartmodel id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ecommerce_cartmodel ALTER COLUMN id SET DEFAULT nextval('public.ecommerce_cartmodel_id_seq'::regclass);


--
-- Name: ecommerce_checkoutmodel id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ecommerce_checkoutmodel ALTER COLUMN id SET DEFAULT nextval('public.ecommerce_checkoutmodel_id_seq'::regclass);


--
-- Name: ecommerce_hiremodel id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ecommerce_hiremodel ALTER COLUMN id SET DEFAULT nextval('public.ecommerce_hiremodel_id_seq'::regclass);


--
-- Name: ecommerce_packagemodel id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ecommerce_packagemodel ALTER COLUMN id SET DEFAULT nextval('public.ecommerce_packagemodel_id_seq'::regclass);


--
-- Name: ecommerce_productsmodel id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ecommerce_productsmodel ALTER COLUMN id SET DEFAULT nextval('public.ecommerce_productsmodel_id_seq'::regclass);


--
-- Name: ecommerce_purchasemodel id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ecommerce_purchasemodel ALTER COLUMN id SET DEFAULT nextval('public.ecommerce_purchasemodel_id_seq'::regclass);


--
-- Name: home_category id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.home_category ALTER COLUMN id SET DEFAULT nextval('public.home_category_id_seq'::regclass);


--
-- Name: home_transaction id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.home_transaction ALTER COLUMN id SET DEFAULT nextval('public.home_transaction_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can view permission	1	view_permission
5	Can add group	2	add_group
6	Can change group	2	change_group
7	Can delete group	2	delete_group
8	Can view group	2	view_group
9	Can add content type	3	add_contenttype
10	Can change content type	3	change_contenttype
11	Can delete content type	3	delete_contenttype
12	Can view content type	3	view_contenttype
13	Can add jobmodel	4	add_jobmodel
14	Can change jobmodel	4	change_jobmodel
15	Can delete jobmodel	4	delete_jobmodel
16	Can view jobmodel	4	view_jobmodel
17	Can add labourmodels	5	add_labourmodels
18	Can change labourmodels	5	change_labourmodels
19	Can delete labourmodels	5	delete_labourmodels
20	Can view labourmodels	5	view_labourmodels
21	Can add requests	6	add_requests
22	Can change requests	6	change_requests
23	Can delete requests	6	delete_requests
24	Can view requests	6	view_requests
25	Can add user	7	add_newusermodel
26	Can change user	7	change_newusermodel
27	Can delete user	7	delete_newusermodel
28	Can view user	7	view_newusermodel
29	Can add cart model	8	add_cartmodel
30	Can change cart model	8	change_cartmodel
31	Can delete cart model	8	delete_cartmodel
32	Can view cart model	8	view_cartmodel
33	Can add checkout model	9	add_checkoutmodel
34	Can change checkout model	9	change_checkoutmodel
35	Can delete checkout model	9	delete_checkoutmodel
36	Can view checkout model	9	view_checkoutmodel
37	Can add hire model	10	add_hiremodel
38	Can change hire model	10	change_hiremodel
39	Can delete hire model	10	delete_hiremodel
40	Can view hire model	10	view_hiremodel
41	Can add products model	11	add_productsmodel
42	Can change products model	11	change_productsmodel
43	Can delete products model	11	delete_productsmodel
44	Can view products model	11	view_productsmodel
45	Can add purchase model	12	add_purchasemodel
46	Can change purchase model	12	change_purchasemodel
47	Can delete purchase model	12	delete_purchasemodel
48	Can view purchase model	12	view_purchasemodel
49	Can add category	13	add_category
50	Can change category	13	change_category
51	Can delete category	13	delete_category
52	Can view category	13	view_category
53	Can add transaction	14	add_transaction
54	Can change transaction	14	change_transaction
55	Can delete transaction	14	delete_transaction
56	Can view transaction	14	view_transaction
57	Can add log entry	15	add_logentry
58	Can change log entry	15	change_logentry
59	Can delete log entry	15	delete_logentry
60	Can view log entry	15	view_logentry
61	Can add session	16	add_session
62	Can change session	16	change_session
63	Can delete session	16	delete_session
64	Can view session	16	view_session
65	Can add package model	17	add_packagemodel
66	Can change package model	17	change_packagemodel
67	Can delete package model	17	delete_packagemodel
68	Can view package model	17	view_packagemodel
\.


--
-- Data for Name: authentication_jobmodel; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.authentication_jobmodel (id, job_title, category) FROM stdin;
1	developer	IT
\.


--
-- Data for Name: authentication_labourmodels; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.authentication_labourmodels (id, username, image_link, job_title, rate, work_type, status) FROM stdin;
1	joey	Dignissimos enim qui	tester	2	f	1
2	joey	Deleniti animi mini	developer	44	f	1
3	joey	Sed excepturi occaec	tester	100	f	1
4	admin	Eos omnis nulla reru	tester	25	t	1
6	admin	Quis sint eu sint nu	tester	94	t	1
7	joey	Illo aperiam ab anim	developer	49	t	1
5	admin	Enim ex quia enim do	developer	35	f	0
\.


--
-- Data for Name: authentication_newusermodel; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.authentication_newusermodel (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, phone_no, rating, is_sub, wallet, subscribed_at, package, image) FROM stdin;
2	pbkdf2_sha256$150000$QCuSOb2dnxs8$9q+jgxtgqWJ5oEnTnD8Kvr9D7n0uAuqZlw0k5vOT+54=	2022-10-31 14:20:51.232874+05:30	f	joey	Lars	Copeland	jadywy@mailinator.com	f	t	2022-10-27 19:09:25.258729+05:30	57	0	f	1000	\N	0	https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png
1	pbkdf2_sha256$150000$SH47RNYq5HRZ$s/3m7I3OhRo4UER5Zj5dvkEq4Pjx9g7R+UIIovcylX4=	2022-10-31 14:38:30.469078+05:30	t	admin	sghgthv	dvsffgh	admin@123.com	t	t	2022-10-27 19:06:42.816891+05:30	4526787876	0	t	2980	2022-10-28	1	https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png
3	pbkdf2_sha256$150000$c0RaQCcGvsct$RaluVBOvOZXEd2349TExcNkpqFB1Tgl9DpxQYupe5X4=	2022-10-28 08:51:25.824153+05:30	f	Anna	Clarke	Griffith	dojykuhuky@mailinator.com	f	t	2022-10-28 08:32:23.600505+05:30	91	0	f	0	\N	0	https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png
\.


--
-- Data for Name: authentication_newusermodel_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.authentication_newusermodel_groups (id, newusermodel_id, group_id) FROM stdin;
\.


--
-- Data for Name: authentication_newusermodel_user_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.authentication_newusermodel_user_permissions (id, newusermodel_id, permission_id) FROM stdin;
\.


--
-- Data for Name: authentication_requests; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.authentication_requests (id, username, worker_username, status) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	auth	permission
2	auth	group
3	contenttypes	contenttype
4	authentication	jobmodel
5	authentication	labourmodels
6	authentication	requests
7	authentication	newusermodel
8	ecommerce	cartmodel
9	ecommerce	checkoutmodel
10	ecommerce	hiremodel
11	ecommerce	productsmodel
12	ecommerce	purchasemodel
13	home	category
14	home	transaction
15	admin	logentry
16	sessions	session
17	ecommerce	packagemodel
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-10-27 19:03:47.405685+05:30
3	contenttypes	0002_remove_content_type_name	2022-10-27 19:04:54.951868+05:30
4	auth	0001_initial	2022-10-27 19:04:54.991138+05:30
5	auth	0002_alter_permission_name_max_length	2022-10-27 19:04:55.02278+05:30
6	auth	0003_alter_user_email_max_length	2022-10-27 19:04:55.030653+05:30
7	auth	0004_alter_user_username_opts	2022-10-27 19:04:55.038759+05:30
8	auth	0005_alter_user_last_login_null	2022-10-27 19:04:55.044895+05:30
9	auth	0006_require_contenttypes_0002	2022-10-27 19:04:55.047257+05:30
10	auth	0007_alter_validators_add_error_messages	2022-10-27 19:04:55.054731+05:30
11	auth	0008_alter_user_username_max_length	2022-10-27 19:04:55.067733+05:30
12	auth	0009_alter_user_last_name_max_length	2022-10-27 19:04:55.072908+05:30
13	auth	0010_alter_group_name_max_length	2022-10-27 19:04:55.089474+05:30
14	auth	0011_update_proxy_permissions	2022-10-27 19:04:55.094273+05:30
15	authentication	0001_initial	2022-10-27 19:04:55.137573+05:30
16	ecommerce	0001_initial	2022-10-27 19:05:06.910432+05:30
17	home	0001_initial	2022-10-27 19:05:16.496813+05:30
18	admin	0001_initial	2022-10-27 19:05:51.177553+05:30
19	admin	0002_logentry_remove_auto_add	2022-10-27 19:05:51.193081+05:30
20	admin	0003_logentry_add_action_flag_choices	2022-10-27 19:05:51.201205+05:30
21	sessions	0001_initial	2022-10-27 19:05:51.209445+05:30
22	ecommerce	0002_purchasemodel_order_id	2022-10-28 12:05:13.82242+05:30
23	ecommerce	0003_auto_20221028_0908	2022-10-28 14:39:09.323951+05:30
24	ecommerce	0004_packagemodel	2022-10-31 10:52:30.031417+05:30
25	ecommerce	0005_auto_20221031_0906	2022-10-31 14:36:49.487152+05:30
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
12rzbttvweqjge8ktzti6h4ofezf7ug3	ZmYxNjE1MDQ4NTJjOTc2MDY5Nzk4Nzc2ZWE1YzZkZjcyOGNmYTE1Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiMWRjNGUzNGJmZjI5Mjg5NjEyYzE3YWYyZDE4NTc5OTFlOWY3YjVlIn0=	2022-11-14 14:38:30.47101+05:30
\.


--
-- Data for Name: ecommerce_cartmodel; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.ecommerce_cartmodel (id, product_id, "Product_name", "Price", "Total", "Quantity", "Image", username, cartnumber) FROM stdin;
\.


--
-- Data for Name: ecommerce_checkoutmodel; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.ecommerce_checkoutmodel (id, product_id, "Products", "Total", "Quantity", username) FROM stdin;
\.


--
-- Data for Name: ecommerce_hiremodel; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.ecommerce_hiremodel (id, worker_name, "Hire_name", "Name", "Place", "Work_mode", "Phone", status, job_title, user_status, worker_status, rating) FROM stdin;
\.


--
-- Data for Name: ecommerce_packagemodel; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.ecommerce_packagemodel (id, package_name, validity, cost, image) FROM stdin;
1	Jorden Fields	39	71	Id qui consequuntur
2	Hector Haley	39	96	Culpa accusamus qui
\.


--
-- Data for Name: ecommerce_productsmodel; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.ecommerce_productsmodel (id, "Product_name", "Price", "Quantity", "Image") FROM stdin;
1	Barbara Macdonald	586	477	Magna cum cupidatat
2	India Day	201	345	Inventore ut eius ma
3	Quon Schultz	278	493	Proident et vel dol
4	Cairo Johnston	954	699	Et omnis elit ipsa
5	Zorita Merritt	626	344	In dolor dolore do d
6	Aurelia Diaz	251	797	Velit nostrud ea nih
\.


--
-- Data for Name: ecommerce_purchasemodel; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.ecommerce_purchasemodel (id, phone, "Total", "Prices", "Quantity", "Product_name", username, first_name, last_name, email, street, building, locality, postal, status, order_id, date) FROM stdin;
\.


--
-- Data for Name: home_category; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.home_category (id, category_name) FROM stdin;
1	IT
\.


--
-- Data for Name: home_transaction; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.home_transaction (id, username, product_name, total_price, date, quantity, "Status") FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 68, true);


--
-- Name: authentication_jobmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.authentication_jobmodel_id_seq', 2, true);


--
-- Name: authentication_labourmodels_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.authentication_labourmodels_id_seq', 7, true);


--
-- Name: authentication_newusermodel_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.authentication_newusermodel_groups_id_seq', 1, false);


--
-- Name: authentication_newusermodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.authentication_newusermodel_id_seq', 3, true);


--
-- Name: authentication_newusermodel_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.authentication_newusermodel_user_permissions_id_seq', 1, false);


--
-- Name: authentication_requests_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.authentication_requests_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 17, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 25, true);


--
-- Name: ecommerce_cartmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ecommerce_cartmodel_id_seq', 1, true);


--
-- Name: ecommerce_checkoutmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ecommerce_checkoutmodel_id_seq', 1, false);


--
-- Name: ecommerce_hiremodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ecommerce_hiremodel_id_seq', 6, true);


--
-- Name: ecommerce_packagemodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ecommerce_packagemodel_id_seq', 2, true);


--
-- Name: ecommerce_productsmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ecommerce_productsmodel_id_seq', 6, true);


--
-- Name: ecommerce_purchasemodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ecommerce_purchasemodel_id_seq', 1, false);


--
-- Name: home_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.home_category_id_seq', 1, true);


--
-- Name: home_transaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.home_transaction_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: authentication_jobmodel authentication_jobmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_jobmodel
    ADD CONSTRAINT authentication_jobmodel_pkey PRIMARY KEY (id);


--
-- Name: authentication_labourmodels authentication_labourmodels_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_labourmodels
    ADD CONSTRAINT authentication_labourmodels_pkey PRIMARY KEY (id);


--
-- Name: authentication_newusermodel_groups authentication_newusermo_newusermodel_id_group_id_84496ce6_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_newusermodel_groups
    ADD CONSTRAINT authentication_newusermo_newusermodel_id_group_id_84496ce6_uniq UNIQUE (newusermodel_id, group_id);


--
-- Name: authentication_newusermodel_user_permissions authentication_newusermo_newusermodel_id_permissi_d69215ca_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_newusermodel_user_permissions
    ADD CONSTRAINT authentication_newusermo_newusermodel_id_permissi_d69215ca_uniq UNIQUE (newusermodel_id, permission_id);


--
-- Name: authentication_newusermodel_groups authentication_newusermodel_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_newusermodel_groups
    ADD CONSTRAINT authentication_newusermodel_groups_pkey PRIMARY KEY (id);


--
-- Name: authentication_newusermodel authentication_newusermodel_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_newusermodel
    ADD CONSTRAINT authentication_newusermodel_pkey PRIMARY KEY (id);


--
-- Name: authentication_newusermodel_user_permissions authentication_newusermodel_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_newusermodel_user_permissions
    ADD CONSTRAINT authentication_newusermodel_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: authentication_newusermodel authentication_newusermodel_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_newusermodel
    ADD CONSTRAINT authentication_newusermodel_username_key UNIQUE (username);


--
-- Name: authentication_requests authentication_requests_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_requests
    ADD CONSTRAINT authentication_requests_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: ecommerce_cartmodel ecommerce_cartmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ecommerce_cartmodel
    ADD CONSTRAINT ecommerce_cartmodel_pkey PRIMARY KEY (id);


--
-- Name: ecommerce_checkoutmodel ecommerce_checkoutmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ecommerce_checkoutmodel
    ADD CONSTRAINT ecommerce_checkoutmodel_pkey PRIMARY KEY (id);


--
-- Name: ecommerce_hiremodel ecommerce_hiremodel_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ecommerce_hiremodel
    ADD CONSTRAINT ecommerce_hiremodel_pkey PRIMARY KEY (id);


--
-- Name: ecommerce_packagemodel ecommerce_packagemodel_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ecommerce_packagemodel
    ADD CONSTRAINT ecommerce_packagemodel_pkey PRIMARY KEY (id);


--
-- Name: ecommerce_productsmodel ecommerce_productsmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ecommerce_productsmodel
    ADD CONSTRAINT ecommerce_productsmodel_pkey PRIMARY KEY (id);


--
-- Name: ecommerce_purchasemodel ecommerce_purchasemodel_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ecommerce_purchasemodel
    ADD CONSTRAINT ecommerce_purchasemodel_pkey PRIMARY KEY (id);


--
-- Name: home_category home_category_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.home_category
    ADD CONSTRAINT home_category_pkey PRIMARY KEY (id);


--
-- Name: home_transaction home_transaction_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.home_transaction
    ADD CONSTRAINT home_transaction_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: authentication_newusermode_newusermodel_id_4c843c60; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX authentication_newusermode_newusermodel_id_4c843c60 ON public.authentication_newusermodel_user_permissions USING btree (newusermodel_id);


--
-- Name: authentication_newusermode_permission_id_fc606b82; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX authentication_newusermode_permission_id_fc606b82 ON public.authentication_newusermodel_user_permissions USING btree (permission_id);


--
-- Name: authentication_newusermodel_groups_group_id_c1da9373; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX authentication_newusermodel_groups_group_id_c1da9373 ON public.authentication_newusermodel_groups USING btree (group_id);


--
-- Name: authentication_newusermodel_groups_newusermodel_id_bd7e3661; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX authentication_newusermodel_groups_newusermodel_id_bd7e3661 ON public.authentication_newusermodel_groups USING btree (newusermodel_id);


--
-- Name: authentication_newusermodel_username_cf3bbbae_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX authentication_newusermodel_username_cf3bbbae_like ON public.authentication_newusermodel USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_newusermodel_groups authentication_newus_group_id_c1da9373_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_newusermodel_groups
    ADD CONSTRAINT authentication_newus_group_id_c1da9373_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_newusermodel_user_permissions authentication_newus_newusermodel_id_4c843c60_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_newusermodel_user_permissions
    ADD CONSTRAINT authentication_newus_newusermodel_id_4c843c60_fk_authentic FOREIGN KEY (newusermodel_id) REFERENCES public.authentication_newusermodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_newusermodel_groups authentication_newus_newusermodel_id_bd7e3661_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_newusermodel_groups
    ADD CONSTRAINT authentication_newus_newusermodel_id_bd7e3661_fk_authentic FOREIGN KEY (newusermodel_id) REFERENCES public.authentication_newusermodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_newusermodel_user_permissions authentication_newus_permission_id_fc606b82_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authentication_newusermodel_user_permissions
    ADD CONSTRAINT authentication_newus_permission_id_fc606b82_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_authentic FOREIGN KEY (user_id) REFERENCES public.authentication_newusermodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

